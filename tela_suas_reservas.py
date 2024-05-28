import tkinter as tk
from io import BytesIO
from tkinter import messagebox

import customtkinter as ctk
import requests
from PIL import Image


class TelaSuasReservas:
    def __init__(self, tela_suas_reservas, banco, email):
        self.tela_suas_reservas = tela_suas_reservas
        self.banco = banco
        self.email = email

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
        leaguespartan_font2 = ctk.CTkFont(family='League Spartan', size=13, weight='normal')

        self.menu_frame = ctk.CTkFrame(tela_suas_reservas, fg_color='#274598', height=160, corner_radius=0, width=300)
        self.menu_frame.grid(column=0, row=0)
        self.menu_frame.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        url = 'https://github.com/marcella2808/UniReservas/blob/master/imagens/unireservas_logo_branco.png?raw=true'
        response = requests.get(url)
        unireservas_logo = ctk.CTkImage(Image.open(BytesIO(response.content)), size=(200, 60))
        unireservas_logo_lbl = ctk.CTkLabel(self.menu_frame, text='', image=unireservas_logo)
        unireservas_logo_lbl.grid(column=0, row=0)
        unireservas_logo_lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font)
        self.suas_reservas_btn.place(rely=0.72, relx=0)

        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff', fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=150, height=47, cursor='hand2', font=leaguespartan_font, command=self.abrir_tela_novas_reservas)
        self.novas.place(rely=0.72, relx=0.502)

        self.reservas_frame = ctk.CTkFrame(tela_suas_reservas, fg_color='#fff', height=200)
        self.reservas_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        id_usuario = self.banco.buscar_id_usuario(email)
        self.reservas = self.banco.listar_reservas_usuario(id_usuario)

        for reserva in self.reservas:
            data, hora_inicio, hora_fim, id_lab = reserva
            reserva_frame = ctk.CTkFrame(self.reservas_frame, fg_color='#f0f0f0', corner_radius=10)
            reserva_frame.pack(pady=10, padx=10, fill="x")

            data_lbl = ctk.CTkLabel(reserva_frame, text=f"Lab {id_lab}    {data}    {hora_inicio}", text_color='#494949', font=leaguespartan_font2)
            data_lbl.pack(anchor='w', padx=10, pady=5)

    def abrir_tela_novas_reservas(self):
        from tela_novas_reservas import TelaNovasReservas
        self.tela_suas_reservas.withdraw()
        tela_novas_reservas = ctk.CTkToplevel()
        TelaNovasReservas(tela_novas_reservas, self.tela_suas_reservas, self.banco, self.email)
        self.tela_suas_reservas.wait_window(tela_novas_reservas)
