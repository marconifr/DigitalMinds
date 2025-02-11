# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Expor a porta 8000
EXPOSE 8000

# Comando para rodar o aplicativo
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]