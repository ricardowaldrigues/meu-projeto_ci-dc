# Imagem base
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de dependência e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta que a aplicação utiliza
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]





