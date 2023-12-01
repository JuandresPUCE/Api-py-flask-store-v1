# Usar una imagen base de Alpine
FROM alpine:3.18

# Instalar Python y pip
RUN apk add --no-cache python3 py-pip

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python3", "src/app.py"]