import sqlite3


class BancoDeDados:
    def __init__(self, nome_banco):  # construtor
        self.nome_banco = nome_banco  # define nome do banco
        self.conn = None  # permite realizar a conexão com o banco de dados (sqlite)
        self.cursor = None  # permite a execução de comandos SQL
        self.criar_tabela_usuarios()
        self.criar_tabela_laboratorios()
        self.criar_tabela_reservas()

    def conectar(self):  # método para conectar com o banco de dados
        self.conn = sqlite3.connect(self.nome_banco)  # cria uma instância de conn
        self.cursor = self.conn.cursor()  # cria uma instância de cursor

    def criar_tabela_usuarios(self):  # cria uma tabela para poder inserir os dados (usuário e senha)
        self.conectar()  # conecta com o banco
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY, 
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                senha TEXT NOT NULL)''')  # executa o comando SQL de criar tabela
        self.conn.commit()  # salva alterações
        self.desconectar()

    def criar_tabela_laboratorios(self): #Cria a tabela de laboratorios 
        self.conectar()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS laboratorios (
                                    id INTEGER PRIMARY KEY,
                                    tipo TEXT NOT NULL,
                                    numero_lab INTEGER NOT NULL
                                    )''')
        self.adicionar_labs()
        self.conn.commit()
        self.desconectar()
    
    def adicionar_labs(self): # adiciona laboratórios na tabela, se ainda não existirem
        self.conectar()
        self.cursor.execute("SELECT COUNT(*) FROM laboratorios")
        count = self.cursor.fetchone()[0]

        if count == 0: # verifica se já existem laboratórios cadastrados
            labs = [
                ("Lab 1", 1),  # Dados do laboratório 1
                ("Lab 2", 2),  # Dados do laboratório 2
                ("Lab 3", 3),  # Dados do laboratório 3
                ("Lab 4", 4),  # Dados do laboratório 4
                ("Lab 5", 5),  # Dados do laboratório 5
                ("Lab 6", 6),  # Dados do laboratório 6
                ("Lab 7", 7)  # Dados do laboratório 7
            ]
            self.cursor.executemany("INSERT INTO laboratorios (tipo, numero_lab) VALUES (?, ?)", labs)

    def criar_tabela_reservas(self): #Cria a tabela para as reservas
        self.conectar()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                            id INTEGER PRIMARY KEY,
                            id_usuario INTEGER,
                            id_laboratorio INTEGER,
                            data TEXT,
                            hora_inicio TEXT,
                            hora_fim TEXT,
                            FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                            FOREIGN KEY (id_laboratorio) REFERENCES laboratorio(id)
                            )''')
        self.conn.commit()
        self.desconectar()

    def adicionar_usuario(self, nome, email, senha): # adiciona um usuário na tabela
        self.conectar()
        self.cursor.execute('''INSERT INTO usuarios(nome, email, senha) VALUES (?, ?, ?)''', (nome, email, senha))
        self.conn.commit()
        self.desconectar()

    def adicionar_reserva(self, id_usuario, id_laboratorio, data, hora_inicio, hora_fim):   # adiciona uma reserva na tabela
        self.conectar()
        self.cursor.execute(
            "INSERT INTO reservas (id_usuario, id_laboratorio, data, hora_inicio, hora_fim) VALUES (?, ?, ?, ?, ?)", (id_usuario, id_laboratorio, data, hora_inicio, hora_fim))
        self.conn.commit()
        self.desconectar()

    def buscar_id_usuario(self, email): # busca o ID de um usuário pelo email
        self.conectar()
        self.cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return None

    def buscar_id_laboratorio(self, lab_tipo):  # busca o ID de um laboratório pelo tipo
        self.cursor.execute("SELECT id FROM laboratorios WHERE tipo = ?", (lab_tipo,))
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return None

    def contar_reservas_usuario(self, id_usuario): # conta o número de reservas de um usuário
        self.conectar()
        self.cursor.execute("SELECT COUNT(*) FROM reservas WHERE id_usuario = ?", (id_usuario,))
        result = self.cursor.fetchone()[0]
        return result

    def listar_reservas_usuario(self, id_usuario): # lista todas as reservas de um usuário
        self.conectar()
        self.cursor.execute("SELECT id, data, hora_inicio, hora_fim, id_laboratorio FROM reservas WHERE id_usuario = ?",
                            (id_usuario,))
        reservas = self.cursor.fetchall()
        self.desconectar()
        return reservas

    def buscar_reservas_por_email(self, email): # busca reservas pelo email do usuário
        self.conectar()
        self.cursor.execute('''
            SELECT reservas.id, reservas.data, reservas.hora_inicio, reservas.hora_fim, reservas.id_laboratorio 
            FROM reservas
            JOIN usuarios ON reservas.id_usuario = usuarios.id
            WHERE usuarios.email = ?
        ''', (email,))
        reservas = self.cursor.fetchall()
        self.desconectar()
        return reservas

    def deletar_reserva(self, id_reserva): # deleta uma reserva pelo ID
        self.conectar()
        self.cursor.execute('''DELETE FROM reservas WHERE id = ?''', (id_reserva,))
        self.conn.commit()
        self.desconectar()

    def validar_login(self, email, senha): # valida o login de um usuário
        self.conectar()
        self.cursor.execute('''SELECT * FROM usuarios WHERE email = ? AND senha = ?''',
                            (email, senha))  # realiza uma consulta
        usuario = self.cursor.fetchone()  # retorna os dados de usuário. Caso não houver, retorna None
        self.desconectar()
        return usuario is not None  # retorna True se usuario existir ou Falso se não existir

    def validar_email(self, email):  # verifica se um email já está cadastrado
        self.conectar()
        self.cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = self.cursor.fetchone()
        self.desconectar()
        return usuario is not None

    def desconectar(self): # desconecta do banco de dados
        self.conn.close()
