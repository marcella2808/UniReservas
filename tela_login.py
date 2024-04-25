import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


class TelaLogin:
    def __init__(self, tela_login, banco):
        self.tela_login = tela_login
        self.banco = banco
        self.tela_login.title('Tela de Login')
        self.tela_login.configure(fg_color="#3F7CA0")

        self.frame = ctk.CTkFrame(tela_login, fg_color="#3F7CA0")
        self.frame.grid(column=0, row=0)

        # fontes
        jejugothic_font = ctk.CTkFont(family="Jeju Gothic", size=12)

        # email label
        self.email_lbl = ctk.CTkLabel(self.frame, text="Digite seu e-mail", text_color="#ffffff", font=jejugothic_font)
        self.email_lbl.grid(column=0, row=0, pady=(0, 2), sticky='w')

        # email entry
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text="E-mail...", placeholder_text_color="#959595", text_color="#000000", corner_radius=20, fg_color="#f0f0f0", border_width=0, width=200, height=30, font=jejugothic_font)
        self.email_entry.grid(column=0, row=1, pady=(0, 10))

        # senha label
        self.senha_lbl = ctk.CTkLabel(self.frame, text="Digite sua senha", text_color="#ffffff", font=jejugothic_font)
        self.senha_lbl.grid(column=0, row=2, pady=(0, 2), sticky='w')

        # senha entry
        self.senha_entry = ctk.CTkEntry(self.frame, show='*', placeholder_text="Senha...", placeholder_text_color="#959595", text_color="#000000", corner_radius=20, fg_color="#f0f0f0", border_width=0, width=200, height=30, font=jejugothic_font)
        self.senha_entry.grid(column=0, row=3, pady=(0, 15))

        # login button
        self.login_btn = ctk.CTkButton(self.frame, text='Entrar', command=self.realizar_login, fg_color="#2E2D71", corner_radius=20, width=200, height=30, cursor="hand2", font=jejugothic_font)
        self.login_btn.grid(column=0, row=4, pady=(0, 10))

        # cadastro button
        self.cadastro_btn = ctk.CTkButton(self.frame, text='Cadastre-se', text_color="#2E2D71", command=self.registrar, fg_color="#3F7CA0", corner_radius=20, border_width=1, border_color="#2E2D71", width=200, height=30, cursor="hand2", font=jejugothic_font)
        self.cadastro_btn.grid(column=0, row=5, pady=(0, 10))

        # esqueceu senha botão
        self.esqueceu_senha_btn = ctk.CTkButton(self.frame, text='Esqueceu sua senha?', text_color="#ffffff", font=jejugothic_font, fg_color="#3F7CA0", corner_radius=20, cursor="hand2")
        self.esqueceu_senha_btn.grid(column=0, row=6)

        self.frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.banco.criar_tabela()

    def realizar_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if self.banco.validar_login(email, senha):
            messagebox.showinfo('Login', 'Login bem sucedido!')
        else:
            messagebox.showerror('Login', 'Usuário ou senha incorretos.')

    def registrar(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.banco.adicionar_usuario(email, senha)
        messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso!')
