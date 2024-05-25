from io import BytesIO

import customtkinter as ctk
import tkinter as tk

import requests
from PIL import Image
from tkinter import messagebox


class TelaEsqueceuSenha:
    def __init__(self, tela_esqueceu_senha, banco, tela_login):
        self.tela_esqueceu_senha = tela_esqueceu_senha
        self.banco = banco
        self.tela_login = tela_login
        self.tela_esqueceu_senha.title('Recuperar senha')
        self.tela_esqueceu_senha.configure(fg_color='#fff')

        # dimensões da janela
        largura = 300
        altura = 575
        x = (self.tela_esqueceu_senha.winfo_screenwidth() - largura) // 2
        y = (self.tela_esqueceu_senha.winfo_screenheight() - altura) // 2
        self.tela_esqueceu_senha.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)
        leaguespartan_font = ctk.CTkFont(family='League Spartan', size=20, weight='bold')

        # imagem do logotipo
        url = 'https://github.com/marcella2808/UniReservas/blob/master/imagens/unireservas_logo_azul.png?raw=true'
        response = requests.get(url)
        unireservas_logo = ctk.CTkImage(Image.open(BytesIO(response.content)), size=(200, 60))
        unireservas_logo_lbl = ctk.CTkLabel(self.tela_esqueceu_senha, text='', image=unireservas_logo)
        unireservas_logo_lbl.grid(column=0, row=0)
        unireservas_logo_lbl.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        # frame para agrupar widgets
        self.frame = ctk.CTkFrame(tela_esqueceu_senha, fg_color='#fff', width=200)
        self.frame.grid(column=0, row=0)

        # título
        self.recuperar_senha_lbl = ctk.CTkLabel(self.frame, text='Recuperar senha', font=leaguespartan_font, text_color='#2E2D71')
        self.recuperar_senha_lbl.grid(column=0, row=1, pady=(0, 20))

        # texto
        self.recuperar_senha_txt_lbl = ctk.CTkLabel(self.frame, text='Para recuperar sua senha, preencha \no campo com seu e-mail cadastrado.', font=jejugothic_font, text_color='#1B444E')
        self.recuperar_senha_txt_lbl.grid(column=0, row=2, pady=(0, 35))

        # legenda "e-mail"
        self.email_lbl = ctk.CTkLabel(self.frame, text='Digite seu e-mail', font=jejugothic_font, text_color='#1B444E')
        self.email_lbl.grid(column=0, row=3, sticky='w', pady=(0, 2))

        # campo de entrada para e-mail
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text='E-mail...', placeholder_text_color='#aaa', text_color='#505050', corner_radius=20, fg_color='#f0f0f0', border_width=0, height=30, font=jejugothic_font)
        self.email_entry.grid(column=0, row=4, pady=(0, 20), sticky='we')

        # botão de enviar e-mail
        self.enviar_email_btn = ctk.CTkButton(self.frame, text='Enviar', text_color='#fff', fg_color='#2E2D71', hover_color='#474691', corner_radius=20, height=30, cursor='hand2', font=jejugothic_font, command=self.enviar_email)
        self.enviar_email_btn.grid(column=0, row=5, pady=(0, 15), sticky='we')

        # botão de voltar à tela de login
        self.voltar_tela_login_btn = ctk.CTkButton(self.frame, text='Voltar', text_color='#505050', fg_color='#fff', hover_color='#ddd', corner_radius=20, width=70, height=30, cursor='hand2', font=jejugothic_font, command=self.voltar_tela_login)
        self.voltar_tela_login_btn.grid(column=0, row=6, sticky='we')

        # posiciona o frame na tela
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # volta à tela de login
    def voltar_tela_login(self):
        self.tela_esqueceu_senha.withdraw()  # Ocultar a janela de recuperação de senha
        self.tela_login.deiconify()

    # mostra pop up de confirmação de envio de email
    def enviar_email(self):
        email = self.email_entry.get()
        if self.banco.validar_email(email):
            messagebox.showinfo('Recuperar senha', 'E-mail enviado com sucesso!')
            self.voltar_tela_login()
        elif email.strip() == '':
            messagebox.showerror('Recuperar senha', 'Por favor, preencha o campo.')
        else:
            messagebox.showerror('Recuperar senha', 'Esse e-mail não está cadastrado.')
