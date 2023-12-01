# Usar una imagen base de Alpine
FROM alpine:3.18

# Instalar Python y pip
RUN apk add --no-cache python3 py3-pip

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .


# Comando para ejecutar la aplicación
CMD ["python3", "src/app.py"]
