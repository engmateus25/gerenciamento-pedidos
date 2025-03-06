# Usando a imagem do Node.js
FROM node:20-alpine

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando arquivos package.json e package-lock.json para instalar as dependências
COPY package*.json ./
RUN npm install


# Copiando todos os arquivos restantes do frontend para o container
COPY . .

# Expondo a porta 3000 (a porta padrão do Next.js)
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["npm", "run", "dev"]
