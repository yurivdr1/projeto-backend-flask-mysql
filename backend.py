import os
from dotenv import load_dotenv

load_dotenv()


from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def obter_conexao():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def criar_tabela():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

criar_tabela()

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(dados)

@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    novo_usuario = request.get_json()
    nome = novo_usuario.get("nome")
    email = novo_usuario.get("email")

    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201

if __name__ == "__main__":
    app.run(debug=True)