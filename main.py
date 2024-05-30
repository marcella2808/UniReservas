import customtkinter as ctk
from banco_dados import BancoDeDados
from tela_login import TelaLogin

# cria janela de login
login = ctk.CTk()

# cria objeto de BancoDeDados
banco = BancoDeDados('unireservas.db')

# cria objeto da tela de login
tela_login = TelaLogin(login, banco)

# roda a aplicação
login.mainloop()
