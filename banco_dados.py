import sqlite3


class BancoDeDados:
    def __init__(self, nome_banco):  # construtor
        self.nome_banco = nome_banco  # define nome do banco
        self.conn = None  # permite realizar a conexão com o banco de dados (sqlite)
        self.cursor = None  # permite a execução de comandos SQL

    def conectar(self):  # método para conectar com o banco de dados
        self.conn = sqlite3.connect(self.nome_banco)  # cria uma instância de conn
        self.cursor = self.conn.cursor()  # cria uma instância de cursor

    def criar_tabela(self):  # cria uma tabela para poder inserir os dados (usuário e senha)
        self.conectar()  # conecta com o banco
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios ( 
                                id INTEGER PRIMARY KEY,
                                email TEXT NOT NULL,
                                senha TEXT NOT NULL)''')  # executa o comando SQL de criar tabela
        self.conn.commit()  # salva alterações
        self.desconectar()  # desconecta do banco

    def adicionar_usuario(self, email, senha):
        self.conectar()
        self.cursor.execute('''INSERT INTO usuarios (email, senha) VALUES (?, ?)''', (email, senha))
        self.conn.commit()
        self.desconectar()

    def validar_login(self, email, senha):
        self.conectar()
        self.cursor.execute('''SELECT * FROM usuarios WHERE email = ? AND senha = ?''', (email, senha))  # realiza uma consulta
        usuario = self.cursor.fetchone()  # retorna os dados de usuário. Caso não houver, retorna None
        self.desconectar()
        return usuario is not None  # retorna True se usuario existir ou Falso se não existir

    def validar_email(self, email):
        self.conectar()
        self.cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = self.cursor.fetchone()
        self.desconectar()
        return usuario is not None

    def desconectar(self):
        self.conn.close()
