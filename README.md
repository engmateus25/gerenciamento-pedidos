# Gerenciamento de Pedidos de Restaurante

## Sobre o Projeto
Este é um sistema para gerenciar pedidos em um restaurante, permitindo criar pedidos, associá-los a mesas, listar mesas e seus pedidos e fechar contas.

## Tecnologias Utilizadas

### Backend:
- **FastAPI** (Framework para a API)
- **MariaDB** (Banco de dados relacional)
- **SQLAlchemy** (ORM para manipulação do banco)
- **Alembic** (Migrations para o banco de dados)

### Frontend:
- **React + Next.js** (Framework para a interface do usuário)
- **Estilização:** Styled Components + PrimeReact
- **Axios** (Requisições HTTP para o backend)

### Docker (Não implementado completamente)
- A intenção era containerizar a aplicação com `Dockerfile` e `docker-compose.yml` para gerenciar os serviços (FastAPI + MariaDB + Frontend). Esta funcionalidade não foi concluída.


## Como Rodar o Projeto

### 1️ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/gerenciamento-pedidos.git
cd gerenciamento-pedidos
```

### 2️ Configurar o Backend
1. Criar um ambiente virtual e instalar dependências:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. Configurar o Banco de Dados (MariaDB)
instale o MariaDB, crie usuário, um banco chamado `restaurant` e as tabelas.
```bash
mysql -u (seu_usuário) -p
```

```sql
CREATE DATABASE restaurant;

USE restaurant;

CREATE TABLE tables (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(50) DEFAULT 'aberta'
);

CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL  -- Preço armazenado em centavos (ex: 100 = R$1,00)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    table_id INT NOT NULL,
    total_price INT NOT NULL,  -- Total em centavos
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (table_id) REFERENCES tables(id) ON DELETE CASCADE
);

CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    menu_item_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(id) ON DELETE CASCADE
);
```

2. Criar as tabelas no banco de dados
```bash
alembic upgrade head
```

2. Adicione seus dados de conexão em dois arquivos
No arquivo alembic.ini, exemplo: sqlalchemy.url = mysql+pymysql://user1:123@localhost:3306/restaurant

No arquivo .env, exemplo: 
DB_USER=user1
DB_PASSWORD=123
DB_HOST=localhost  
DB_PORT=3306
DB_NAME=restaurant

3. Popular o banco
Compile o arquivo abaixo, para inserir 5 mesas e os itens do menu.
```bash
python -m app.populate_db
```

4. Rodar o servidor FastAPI:
```bash
uvicorn main:app --reload
```
A API estará disponível em: [http://localhost:8080/docs](http://localhost:8080/docs)
se der erro, vá para a porta: [http://localhost:8000/docs](http://localhost:8080/docs)

### 3️ Configurar o Frontend
1. Instalar dependências:
```bash
cd frontend
npm install
```
2. Rodar o projeto:
```bash
npm run dev
```
O frontend estará disponível em: [http://localhost:3000](http://localhost:3000)
se der erro, vá para a porta: [http://localhost:3001](http://localhost:3001)

É só recaregar a página, para ver as alterações realizadas a cada novo pedido ou fechamento de conta.

Imagens da Interface:
![alt text](image-1.png)
![alt text](image-2.png)

## Funcionalidades Implementadas
✅ Criar pedidos e vincular a mesas
✅ Listar pedidos e mesas
✅ Fechar contas e remover pedidos de mesas fechadas
✅ Interface Intuitiva
✅ Backend estruturado com FastAPI e banco de dados MariaDB

## Funcionalidades Pendentes
❌ **Dockerização completa**: O `Dockerfile` e `docker-compose.yml` não foram finalizados.
❌ **Resumo de vendas diárias**: O endpoint `/orders/summary` não faz o resumo de vendas do dia.

## Considerações Finais
Este projeto cumpre a maior parte dos requisitos do teste, oferecendo um sistema funcional de gerenciamento de pedidos para restaurantes. Melhorias futuras podem incluir a implementação completa do Docker e a adição do resumo de vendas diárias.

**Autor:** Mateus de Jesus  
**Data:** Março de 2025
