import tkinter as tk
import customtkinter as ctk
from PIL import Image


class TelaSuasReservas:
    def __init__(self, tela_suas_reservas):
        self.tela_suas_reservas = tela_suas_reservas

        self.tela_suas_reservas.title('Suas reservas')
        self.tela_suas_reservas.configure(fg_color='#fff')

        largura = 300
        altura = 575
        x = (self.tela_suas_reservas.winfo_screenwidth() - largura) // 2
        y = (self.tela_suas_reservas.winfo_screenheight() - altura) // 2
        self.tela_suas_reservas.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)
        leaguespartan_font = ctk.CTkFont(family='League Spartan', size=13, weight='bold')

        self.menu_frame = ctk.CTkFrame(tela_suas_reservas, fg_color='#274598', height=160, corner_radius=0, width=300)
        self.menu_frame.grid(column=0, row=0)
        self.menu_frame.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        unireservas_logo = ctk.CTkImage(Image.open('imagens/unireservas_logo_branco.png'), size=(170, 51))
        unireservas_logo_lbl = ctk.CTkLabel(self.menu_frame, text="", image=unireservas_logo)
        unireservas_logo_lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font)
        self.suas_reservas_btn.place(rely=0.72, relx=0)

        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff',
                                               fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=150,
                                               height=47, cursor='hand2', font=leaguespartan_font, command=self.abrir_tela_novas_reservas)
        self.novas.place(rely=0.72, relx=0.502)

    def abrir_tela_novas_reservas(self):
        from tela_novas_reservas import TelaNovasReservas
        self.tela_suas_reservas.withdraw()
        tela_novas_reservas = ctk.CTkToplevel()
        TelaNovasReservas(tela_novas_reservas, self.tela_suas_reservas)
        self.tela_suas_reservas.wait_window(tela_novas_reservas)