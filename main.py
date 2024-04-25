import customtkinter as ctk
from banco_dados import BancoDeDados
from tela_login import TelaLogin

# Criar a janela principal
login = ctk.CTk()

# Criar objeto do banco de dados
banco = BancoDeDados('usuarios.db')

# Criar objeto da tela de login
tela_login = TelaLogin(login, banco)

# Rodar a aplicação
login.mainloop()
