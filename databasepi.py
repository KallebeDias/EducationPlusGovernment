import sqlite3
import hashlib

# Função para hash de senha (para segurança básica)
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para conectar ao banco de dados
def conectar_bd():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    # Criar tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

# Função para cadastrar usuário
def cadastrar_usuario(username, senha):
    conn, cursor = conectar_bd()
    try:
        hashed = hash_senha(senha)
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Usuário já existe
    finally:
        conn.close()

# Função para verificar login
def verificar_login(username, senha):
    conn, cursor = conectar_bd()
    try:
        hashed = hash_senha(senha)
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, hashed))
        usuario = cursor.fetchone()
        return usuario is not None
    finally:
        conn.close()
