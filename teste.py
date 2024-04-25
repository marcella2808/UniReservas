import customtkinter as ctk


def clique():
    print("Fazer login")


janela = ctk.CTk()
janela.geometry("500x300")

janela.title("Login")

texto = ctk.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = ctk.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = ctk.CTkEntry(janela, placeholder_text="Sua senha", show='*')
senha.pack(padx=10, pady=10)

botao = ctk.CTkButton(janela, text="Login", command=clique, fg_color="#3F7CA0")
botao.pack(padx=10, pady=10)

janela.mainloop()
