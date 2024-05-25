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

    def criar_tabela_laboratorios(self):
        self.conectar()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS laboratorios (
                                    id INTEGER PRIMARY KEY,
                                    tipo TEXT NOT NULL,
                                    numero_lab INTEGER NOT NULL
                                    )''')
        self.adicionar_labs()
        self.conn.commit()
        self.desconectar()

    def adicionar_labs(self):
        self.conectar()
        self.cursor.execute("SELECT COUNT(*) FROM laboratorios")
        count = self.cursor.fetchone()[0]

        if count == 0:
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

    def criar_tabela_reservas(self):
        self.conectar()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                            id INTEGER PRIMARY KEY,
                            id_usuarios INTEGER,
                            id_laboratorios INTEGER,
                            data TEXT,
                            hora_inicio TEXT,
                            hora_fim TEXT,
                            FOREIGN KEY (id_usuarios) REFERENCES usuarios(id),
                            FOREIGN KEY (id_laboratorios) REFERENCES laboratorios(id)
                            )''')
        self.conn.commit()
        self.desconectar()

    def adicionar_usuario(self, nome, email, senha):
        self.conectar()
        self.cursor.execute('''INSERT INTO usuarios(nome, email, senha) VALUES (?, ?, ?)''', (nome, email, senha))
        self.conn.commit()
        self.desconectar()

    '''def adicionar_reserva(self, email):
        self.conectar()
        self.cursor.execute(''''SELECT * FROM usuarios WHERE email = ?'''', (email,))
        id_usuario = self.cursor.fetchone()[0]
        from tela_labs_disponiveis import TelaLabsDisponiveis
        from tela_novas_reservas import TelaNovasReservas
        tela_novas = TelaNovasReservas(tela_novas_reservas=None, tela_suas_reservas=None)
        data = tela_novas.calendario.get_date()
        hora_inicio = tela_novas.hora_inicio_entry.get()
        hora_fim = tela_novas.hora_fim_entry.get()
        tela_labs = TelaLabsDisponiveis(tela_labs_disponiveis=None, data_selecionada=None, hora_inicio_selecionada=None, hora_fim_selecionada=None, tela_novas_reservas=None)
        id_lab = tela_labs.obter_lab_selecionado()

        infos = [
            id_usuario,
            id_lab,
            data,
            hora_inicio,
            hora_fim
        ]

        self.cursor.execute(''''INSERT INTO reservas(id_usuarios, id_laboratorios, data, hora_inicio, hora_fim) VALUES (?,?,?,?,?)'''', infos)
        self.conn.commit()
        self.desconectar()'''

    def validar_login(self, email, senha):
        self.conectar()
        self.cursor.execute('''SELECT * FROM usuarios WHERE email = ? AND senha = ?''',
                            (email, senha))  # realiza uma consulta
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
