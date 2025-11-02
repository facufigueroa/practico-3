import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from persona.models import Persona
from oficina.models import Oficina

def run(*args):
    if not args:
        print("Error: Se requiere la ruta del archivo CSV como argumento.")
        print("Uso: ./manage.py runscript importarPersonas.py --script-args <ruta_del_archivo_csv>")
        sys.exit(1)
    
    csvFilePath = args[0]

    oficinas = {oficina.nombreCorto: oficina for oficina in Oficina.objects.all()}

    try:
        with open(csvFilePath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            personasImportadas = []
            for row in reader:
                nombre = row.get('nombre')
                apellido = row.get('apellido')
                edad = row.get('edad')
                oficinaNombreCorto = row.get('oficinaNombreCorto')

                if not nombre or not apellido or not edad :
                    print(f"Error: Faltan datos en la fila: {row}")
                    continue

                try:
                    edad = int(edad)
                except ValueError:
                    print(f"Error: Edad inválida para la persona {nombre}: {edad}")
                    continue

                oficina = None
                if oficinaNombreCorto:
                    oficina = oficinas.get(oficinaNombreCorto)
                    if not oficina:
                        print(f"Error: No se encontró la oficina con nombre corto '{oficinaNombreCorto}' para la persona {nombre}.")
                        print("Se omitirá la asignación de oficina.")

                try:
                    persona = Persona(nombre=nombre, apellido=apellido, edad=int(edad), oficina=oficina)
                    persona.full_clean()  # Valido el modelo
                    personasImportadas.append(persona)
                except ValidationError as e:
                    print(f"Error de validación para la persona {nombre}: {e}")
                except Exception as e:
                    print(f"Error inesperado para la persona {nombre}: {e}")
            
            with transaction.atomic():
                Persona.objects.bulk_create(personasImportadas)
                print(f"Importación completada: {len(personasImportadas)} personas importadas exitosamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csvFilePath}.")
    except Exception as e:
        print(f"Error inesperado al procesar el archivo: {e}")