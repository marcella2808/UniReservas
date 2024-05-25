from io import BytesIO

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

import requests
from PIL import Image


class TelaLogin:
    def __init__(self, tela_login, banco):
        self.tela_login = tela_login
        self.banco = banco
        self.tela_login.title('Login')
        self.tela_login.configure(fg_color='#3F7CA0')
        self.janela_recuperacao_senha = None

        # dimensões da janela
        largura = 300
        altura = 575
        x = (self.tela_login.winfo_screenwidth() - largura) // 2
        y = (self.tela_login.winfo_screenheight() - altura) // 2
        self.tela_login.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)

        # frame para agrupar widgets
        self.frame = ctk.CTkFrame(tela_login, fg_color='#3F7CA0')
        self.frame.grid(column=0, row=0)

        # imagem do logotipo
        url = 'https://github.com/marcella2808/UniReservas/blob/master/imagens/unireservas_logo_grande.png?raw=true'
        response = requests.get(url)
        unireservas_logo = ctk.CTkImage(Image.open(BytesIO(response.content)), size=(200, 200))
        unireservas_logo_lbl = ctk.CTkLabel(self.frame, text='', image=unireservas_logo)
        unireservas_logo_lbl.grid(column=0, row=0)

        # legenda "Digite seu e-mail"
        self.email_lbl = ctk.CTkLabel(self.frame, text='Digite seu e-mail', text_color='#fff', font=jejugothic_font)
        self.email_lbl.grid(column=0, row=1, pady=(0, 2), sticky='w')

        # campo de entrada para e-mail
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text='E-mail...', placeholder_text_color='#909090', text_color='#505050', corner_radius=20, fg_color='#f0f0f0', border_width=0, width=200, height=30, font=jejugothic_font)
        self.email_entry.grid(column=0, row=2, pady=(0, 5))

        # legenda "Digite sua senha"
        self.senha_lbl = ctk.CTkLabel(self.frame, text='Digite sua senha', text_color='#fff', font=jejugothic_font)
        self.senha_lbl.grid(column=0, row=3, pady=(0, 2), sticky='w')

        # campo de entrada para senha
        self.senha_entry = ctk.CTkEntry(self.frame, show='*', placeholder_text='Senha...', placeholder_text_color='#909090', text_color='#505050', corner_radius=20, fg_color='#f0f0f0', border_width=0, width=200, height=30, font=jejugothic_font)
        self.senha_entry.grid(column=0, row=4, pady=(0, 20))

        # botão de login
        self.login_btn = ctk.CTkButton(self.frame, text='Entrar', hover_color='#1F1E54', command=self.realizar_login, fg_color='#2E2D71', corner_radius=20, width=200, height=30, cursor='hand2', font=jejugothic_font)
        self.login_btn.grid(column=0, row=5, pady=(0, 10))

        # botão de cadastro
        self.cadastro_btn = ctk.CTkButton(self.frame, text='Cadastre-se', command=self.abrir_tela_cadastro, text_color='#2E2D71', fg_color='#3F7CA0', hover_color='#3B7596', corner_radius=20, border_width=2, border_color='#2E2D71', width=200, height=30, cursor='hand2', font=jejugothic_font)
        self.cadastro_btn.grid(column=0, row=6, pady=(0, 10))

        # botão de esqueceu senha
        self.esqueceu_senha_btn = ctk.CTkButton(self.frame, text='Esqueceu sua senha?', text_color='#fff', hover_color='#3B7596', font=jejugothic_font, fg_color='#3F7CA0', corner_radius=20, cursor='hand2', command=self.abrir_tela_esqueceu_senha)
        self.esqueceu_senha_btn.grid(column=0, row=7, sticky='we')

        # posiciona o frame no centro da janela
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # faz login
    def realizar_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if self.banco.validar_login(email, senha):
            self.abrir_tela_suas_reservas()
        elif email.strip() == '':
            messagebox.showerror('Cadastro', 'Por favor, preencha todos os campos')
        elif senha.strip() == '':
            messagebox.showerror('Cadastro', 'Por favor, preencha todos os campos')
        else:
            messagebox.showerror('Login', 'Usuário ou senha incorretos.')

    def abrir_tela_suas_reservas(self):
        from tela_suas_reservas import TelaSuasReservas
        self.tela_login.withdraw()
        tela_suas_reservas = ctk.CTkToplevel()
        TelaSuasReservas(tela_suas_reservas)
        self.tela_login.wait_window(tela_suas_reservas)

    def abrir_tela_cadastro(self):
        from tela_cadastro import TelaCadastro
        self.tela_login.withdraw()  # Oculta a janela de login
        tela_cadastro = ctk.CTkToplevel()
        TelaCadastro(tela_cadastro, self.banco, self.tela_login)  # Cria a tela de cadastro
        self.tela_login.wait_window(tela_cadastro)  # Aguarda o fechamento da tela de cadastro  # Torna a janela de login visível novamente

    # abre tela de esqueceu senha
    def abrir_tela_esqueceu_senha(self):
        from tela_esqueceu_senha import TelaEsqueceuSenha
        self.tela_login.withdraw()
        tela_esqueceu_senha = ctk.CTkToplevel()
        TelaEsqueceuSenha(tela_esqueceu_senha, self.banco, self.tela_login)
        self.tela_login.wait_window(tela_esqueceu_senha)
