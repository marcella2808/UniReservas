import customtkinter as ctk
from banco_dados import BancoDeDados
from tela_login import TelaLogin

# Criar a janela principal
login = ctk.CTk()

# Definir as dimensões da janela
largura = 300
altura = 575
x = (login.winfo_screenwidth() - largura) // 2
y = (login.winfo_screenheight() - altura) // 2
login.geometry(f"{largura}x{altura}+{x}+{y}")

# Criar objeto do banco de dados
banco = BancoDeDados('usuarios.db')

# Criar objeto da tela de login
tela_login = TelaLogin(login, banco)

# Rodar a aplicação
login.mainloop()
