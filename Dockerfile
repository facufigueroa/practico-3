# Imagen madre
FROM python:3.11-slim

# Configuración para poder ver los logs de manera correcta
ENV PYTHONBUFFERED=1

# Directorio de trabajo
WORKDIR /crud

# Copiar archivo de dependencias
COPY requirements.txt .

# Instala dependencias vía pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente del proyecto dentro de la imagen
COPY crud/ .