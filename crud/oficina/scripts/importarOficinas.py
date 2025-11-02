import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from oficina.models import Oficina

def run(*args):
    if not args:
        print("Error: Se requiere la ruta del archivo CSV como argumento.")
        print("Uso: ./manage.py runscript importarOficinas.py --script-args <ruta_del_archivo_csv>")
        sys.exit(1)
    
    csvFilePath = args[0]
    try:
        with open(csvFilePath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            oficinasImportadas = []
            for row in reader:
                nombre = row.get('nombre')
                nombreCorto = row.get('nombreCorto')

                if not nombre or not nombreCorto:
                    print(f"Error: Faltan datos en la fila: {row}")
                    continue

                try:
                    oficina = Oficina(nombre=nombre, nombreCorto=nombreCorto)
                    oficina.full_clean()  # Valido el modelo
                    oficinasImportadas.append(oficina)
                except ValidationError as e:
                    print(f"Error de validación para la oficina {nombre}: {e}")
                except Exception as e:
                    print(f"Error inesperado para la oficina {nombre}: {e}")
            
            with transaction.atomic():
                Oficina.objects.bulk_create(oficinasImportadas)
                print(f"Importación completada: {len(oficinasImportadas)} oficinas importadas exitosamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csvFilePath}.")
    except Exception as e:
        print(f"Error inesperado al procesar el archivo: {e}")