# 🚀 API REST — Backend Flask + MySQL

API REST desenvolvida em Python utilizando Flask, integrada a um banco de dados MySQL para cadastro e consulta de usuários.

## 🛠️ Tecnologias utilizadas

- Python 3
- Flask
- Flask-CORS
- MySQL
- MySQL Connector
- Python-dotenv

## 📌 Funcionalidades

A API possui as seguintes rotas:

| Método | Endpoint | Funcionalidade |
|---|---|---|
| POST | `/usuarios` | Cadastra um usuário |
| GET | `/usuarios` | Lista os usuários cadastrados |

O cadastro recebe nome e e-mail.

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd projeto-backend-flask-mysql
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o banco de dados

No MySQL, crie o banco:

```sql
CREATE DATABASE seu_banco;
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como modelo.

Configure:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

**Importante:** não compartilhe seu arquivo `.env` nem publique suas credenciais.

### 5. Execute o backend

```bash
python backend.py
```

## 📚 Objetivo do projeto

Projeto desenvolvido com o objetivo de praticar o desenvolvimento backend, a criação de APIs REST, a integração com banco de dados relacionais e a utilização de variáveis de ambiente para proteger informações sensíveis.

## 👨‍💻 Desenvolvedor

Yuri Vador

GitHub: https://github.com/yurivdr1

LinkedIn: https://www.linkedin.com/in/yurivador-dev