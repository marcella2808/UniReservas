import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image


class TelaLogin:
    def __init__(self, tela_login, banco):
        self.tela_login = tela_login
        self.banco = banco
        self.tela_login.title('UniReservas - Login')
        self.tela_login.configure(fg_color="#3F7CA0")
        self.janela_recuperacao_senha = None

        # dimensões da janela
        largura = 300
        altura = 575
        x = (self.tela_login.winfo_screenwidth() - largura) // 2
        y = (self.tela_login.winfo_screenheight() - altura) // 2
        self.tela_login.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        helvetica_font = ctk.CTkFont(family="Helvetica", size=12)
        malgungothic_bold_font = ctk.CTkFont(family="Malgun Gothic", size=12, weight='bold')

        # frame para agrupar widgets
        self.frame = ctk.CTkFrame(tela_login, fg_color="#3F7CA0")
        self.frame.grid(column=0, row=0)

        # imagem do logotipo
        unireservas_logo = ctk.CTkImage(Image.open('imagens/unireservas_logo_grande.png'), size=(200, 200))
        unireservas_logo_lbl = ctk.CTkLabel(self.frame, text="", image=unireservas_logo)
        unireservas_logo_lbl.grid(column=0, row=0)

        # legenda "Digite seu e-mail"
        self.email_lbl = ctk.CTkLabel(self.frame, text="Digite seu e-mail", text_color="#ffffff", font=malgungothic_bold_font)
        self.email_lbl.grid(column=0, row=1, pady=(0, 2), sticky='w')

        # campo de entrada para e-mail
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text="E-mail...", placeholder_text_color="#959595", text_color="#000000", corner_radius=20, fg_color="#f0f0f0", border_width=0, width=200, height=30, font=helvetica_font)
        self.email_entry.grid(column=0, row=2, pady=(0, 5))

        # legenda "Digite sua senha"
        self.senha_lbl = ctk.CTkLabel(self.frame, text="Digite sua senha", text_color="#ffffff", font=malgungothic_bold_font)
        self.senha_lbl.grid(column=0, row=3, pady=(0, 2), sticky='w')

        # campo de entrada para senha
        self.senha_entry = ctk.CTkEntry(self.frame, show='*', placeholder_text="Senha...", placeholder_text_color="#959595", text_color="#000000", corner_radius=20, fg_color="#f0f0f0", border_width=0, width=200, height=30, font=helvetica_font)
        self.senha_entry.grid(column=0, row=4, pady=(0, 20))

        # botão de login
        self.login_btn = ctk.CTkButton(self.frame, text='Entrar', command=self.realizar_login, fg_color="#2E2D71", corner_radius=20, width=200, height=30, cursor="hand2", font=malgungothic_bold_font)
        self.login_btn.grid(column=0, row=5, pady=(0, 10))

        # botão de cadastro
        self.cadastro_btn = ctk.CTkButton(self.frame, text='Cadastre-se', text_color="#2E2D71", command=self.registrar, fg_color="#3F7CA0", corner_radius=20, border_width=1, border_color="#2E2D71", width=200, height=30, cursor="hand2", font=malgungothic_bold_font)
        self.cadastro_btn.grid(column=0, row=6, pady=(0, 10))

        # botão de esqueceu senha
        self.esqueceu_senha_btn = ctk.CTkButton(self.frame, text='Esqueceu sua senha?', text_color="#ffffff", font=malgungothic_bold_font, fg_color="#3F7CA0", corner_radius=20, cursor="hand2", command=self.abrir_tela_esqueceu_senha)
        self.esqueceu_senha_btn.grid(column=0, row=7)

        # posiciona o frame no centro da janela
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # cria tabela de usuários
        self.banco.criar_tabela()

    # faz login
    def realizar_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if self.banco.validar_login(email, senha):
            messagebox.showinfo('Login', 'Login bem sucedido!')
        else:
            messagebox.showerror('Login', 'Usuário ou senha incorretos.')

    # abre tela de esqueceu senha
    def abrir_tela_esqueceu_senha(self):
        from tela_esqueceu_senha import TelaEsqueceuSenha
        self.tela_login.withdraw()  # Ocultar a janela de login
        tela_esqueceu_senha = ctk.CTkToplevel()
        TelaEsqueceuSenha(tela_esqueceu_senha, self.banco, self.tela_login)
        tela_esqueceu_senha.mainloop()

    # registra usuário no banco de dados
    def registrar(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.banco.adicionar_usuario(email, senha)
        messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso!')
