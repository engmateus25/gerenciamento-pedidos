# Usando a imagem oficial do Python
FROM python:3.10

# Instalar o cliente MySQL
RUN apt-get update && apt-get install -y default-mysql-client


# Definindo o diretório de trabalho no container
WORKDIR /app

# Copia apenas os arquivos necessários para instalar dependências primeiro (melhora o cache do Docker)
COPY requirements.txt .

# Instalando dependências antes de copiar o código (evita reinstalar em cada build)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o script wait-for-db.sh para o container
COPY ./wait-for-db.sh /app/wait-for-db.sh

# Dar permissão de execução para o script
RUN chmod +x /app/wait-for-db.sh

# Copia o restante dos arquivos após instalar as dependências
COPY . .

# Expondo a porta do FastAPI
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
