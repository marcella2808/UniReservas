import customtkinter as ctk
import tkinter as tk
from PIL import Image
from tkinter import messagebox


class TelaEsqueceuSenha:
    def __init__(self, tela_esqueceu_senha, banco):
        self.tela_esqueceu_senha = tela_esqueceu_senha
        self.banco = banco
        self.tela_esqueceu_senha.title('UniReservas - Esqueci minha senha')
        self.tela_esqueceu_senha.configure(fg_color="#fff")

        # fonte
        jejugothic_font = ctk.CTkFont(family="JejuGothic", size=12)
        leaguespartan_font = ctk.CTkFont(family='League Spartan', size=20, weight='bold')

        largura = 300
        altura = 575
        x = (self.tela_esqueceu_senha.winfo_screenwidth() - largura) // 2
        y = (self.tela_esqueceu_senha.winfo_screenheight() - altura) // 2
        self.tela_esqueceu_senha.geometry(f"{largura}x{altura}+700+80")

        self.frame = ctk.CTkFrame(tela_esqueceu_senha, fg_color="#fff")
        self.frame.grid(column=0, row=0)

        unireservas_logo_azul = ctk.CTkImage(Image.open('imagens/unireservas_logo_azul.png'), size=(200, 60))
        unireservas_logo_azul_lbl = ctk.CTkLabel(self.tela_esqueceu_senha, text="", image=unireservas_logo_azul)
        unireservas_logo_azul_lbl.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        self.recuperar_senha_lbl = ctk.CTkLabel(self.frame, text="Recuperar senha", font=leaguespartan_font, text_color='#2E2D71')
        self.recuperar_senha_lbl.grid(column=0, row=1, pady=(0, 20))

        self.recuperar_senha_txt_lbl = ctk.CTkLabel(self.frame, text="Para recuperar sua senha, preencha \no campo com seu e-mail.", font=jejugothic_font, text_color='#1B444E')
        self.recuperar_senha_txt_lbl.grid(column=0, row=2, pady=(0, 40))

        self.email_lbl = ctk.CTkLabel(self.frame, text="Digite seu e-mail", font=jejugothic_font, text_color='#1B444E')
        self.email_lbl.grid(column=0, row=3, sticky='w', pady=(0, 2))

        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text="E-mail...", placeholder_text_color="#959595", text_color="#000000", corner_radius=20, fg_color="#f0f0f0", border_width=0, width=200, height=30, font=jejugothic_font)
        self.email_entry.grid(column=0, row=4, pady=(0, 20))

        self.recuperar_senha_btn = ctk.CTkButton(self.frame, text='Enviar', text_color="#fff", fg_color="#2E2D71", corner_radius=20, width=200, height=30, cursor="hand2", font=jejugothic_font, command=self.enviar_email)
        self.recuperar_senha_btn.grid(column=0, row=5)

        self.frame.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

    def enviar_email(self):
        email = self.email_entry.get()

        if self.banco.validar_email(email):
            from UniReservas.tela_login import TelaLogin
            messagebox.showinfo('Recuperar senha', 'E-mail enviado com sucesso!')
            self.tela_esqueceu_senha.destroy()
            login = ctk.CTkToplevel()
            TelaLogin(login, self.banco)
            login.mainloop()
        else:
            messagebox.showerror('Recuperar senha', 'Esse e-mail não está cadastrado.')
