import customtkinter as ctk
import tkinter as tk
from PIL import Image
from tkinter import messagebox


class TelaCadastro:
    def __init__(self, tela_cadastro, banco, tela_login):
        self.tela_login = tela_login
        self.tela_cadastro = tela_cadastro
        self.banco = banco
        self.tela_cadastro.title('Tela de Cadastro')
        self.tela_cadastro.configure(fg_color='#fff')

        # dimensões da janela
        altura = 575
        largura = 300
        x = (self.tela_cadastro.winfo_screenwidth() - largura) // 2
        y = (self.tela_cadastro.winfo_screenheight() - altura) // 2
        self.tela_cadastro.geometry(f"{largura}x{altura}+{x}+{y}")

        # frame para agrupar os widgets
        self.frame = ctk.CTkFrame(tela_cadastro, fg_color='#fff')
        self.frame.grid(column=0, row=0)

        # fontes
        league_spartan = ctk.CTkFont(family='League Spartan', size=20, weight='bold')
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)

        # imagem do logotipo
        unireservas_logo = ctk.CTkImage(Image.open('imagens/unireservas_logo_azul.png'), size=(200, 60))
        unireservas_logo_lbl = ctk.CTkLabel(self.tela_cadastro, text='', image=unireservas_logo)
        unireservas_logo_lbl.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        # título
        self.cadastrar_lbl = ctk.CTkLabel(self.frame, text='Cadastre-se', text_color='#2E2D71', font=league_spartan)
        self.cadastrar_lbl.grid(column=0, row=1, pady=(0, 20))

        # legenda "Digite seu nome"
        self.nome_lbl = ctk.CTkLabel(self.frame, text='Digite seu nome', text_color='#1B444E', font=jejugothic_font)
        self.nome_lbl.grid(column=0, row=2, pady=(0, 2), sticky='w')

        # campo de entrada para nome
        self.nome_entry = ctk.CTkEntry(self.frame, placeholder_text='Nome...', placeholder_text_color='#aaa', fg_color='#F0F0F0', text_color='#505050', corner_radius=20, border_width=0, width=200, height=30, font=jejugothic_font)
        self.nome_entry.grid(column=0, row=3, pady=(0, 5))

        # legenda "Digite seu e-mail"
        self.email_lbl = ctk.CTkLabel(self.frame, text='Digite seu e-mail', text_color='#1B444E', font=jejugothic_font)
        self.email_lbl.grid(column=0, row=6, pady=(0, 2), sticky='w')

        # campo de entrada para e-mail
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text='E-mail...', placeholder_text_color='#aaa', corner_radius=20, text_color='#505050', fg_color='#F0F0F0', border_width=0, width=200, height=30, font=jejugothic_font)
        self.email_entry.grid(column=0, row=7, pady=(0, 5), sticky='w')

        # legenda "Digite sua senha"
        self.senha_lbl = ctk.CTkLabel(self.frame, text='Digite sua senha', text_color='#1B444E', font=jejugothic_font)
        self.senha_lbl.grid(column=0, row=11, pady=(0, 2), sticky='w')

        # campo de entrada para senha
        self.senha_entry = ctk.CTkEntry(self.frame, placeholder_text='Senha...', show='*', placeholder_text_color='#aaa', text_color='#505050', border_width=0, width=200, height=30, fg_color='#F0F0F0', corner_radius=20, font=jejugothic_font)
        self.senha_entry.grid(column=0, row=12, pady=(0, 5), sticky='w')

        # legenda "Confirmar senha"
        self.confirmar_senha_lbl = ctk.CTkLabel(self.frame, text='Confirmar senha', text_color='#1B444E', font=jejugothic_font)
        self.confirmar_senha_lbl.grid(column=0, row=16, pady=(0, 2), sticky='w')

        # campo de entrada para confirmar senha
        self.confirmar_senha_entry = ctk.CTkEntry(self.frame, show='*', placeholder_text='Senha...', placeholder_text_color='#aaa', text_color='#505050', border_width=0, fg_color='#F0F0F0', width=200, height=30, corner_radius=20, font=jejugothic_font)
        self.confirmar_senha_entry.grid(column=0, row=17, pady=(0, 20), sticky='w')

        # botão de cadastrar
        self.cadastrar_btn = ctk.CTkButton(self.frame, text='Solicitar Acesso', text_color='#fff', command=self.cadastrar, fg_color='#2E2D71', corner_radius=20, font=jejugothic_font, height=30)
        self.cadastrar_btn.grid(column=0, row=19, pady=(0, 20), sticky='we')

        # botão de voltar à tela de login
        self.voltar_tela_login_btn = ctk.CTkButton(self.frame, text='Voltar', text_color='#000', command=self.voltar_tela_login, fg_color='#f0f0f0', corner_radius=20, font=jejugothic_font, width=70, height=30)
        self.voltar_tela_login_btn.grid(column=0, row=20, pady=(0, 2), sticky='w')

        # posiciona o frame na tela
        self.frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.banco.criar_tabela_usuarios()

    def cadastrar(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        confirmar_senha = self.confirmar_senha_entry.get()

        if nome.strip() == '':
            messagebox.showerror('Cadastro', 'Por favor, preencha todos os campos')
        elif email.strip() == '':
            messagebox.showerror('Cadastro', 'Por favor, preencha todos os campos')
        elif senha.strip() == '':
            messagebox.showerror('Cadastro', 'Por favor, preencha todos os campos')
        elif confirmar_senha.strip() == '':
            messagebox.showerror('Cadastro', 'Por favor, confirme a senha')
        elif senha != confirmar_senha:
            messagebox.showerror('Cadastro', 'Senhas não compatíveis, tente novamente.')
        else:
            messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso!')
            self.banco.adicionar_usuario(nome, email, senha)
            self.voltar_tela_login()

    def voltar_tela_login(self):
        self.tela_cadastro.withdraw()
        self.tela_login.deiconify()
