import tkinter as tk
import customtkinter as ctk
from PIL import Image


class TelaLabsDisponiveis:
    def __init__(self, tela_labs_disponiveis, data_selecionada, hora_inicio_selecionada, hora_fim_selecionada, tela_novas_reservas):
        self.tela_labs_disponiveis = tela_labs_disponiveis
        self.data_selecionada = data_selecionada
        self.hora_inicio_selecionada = hora_inicio_selecionada
        self.hora_fim_selecionada = hora_fim_selecionada
        self.tela_novas_reservas = tela_novas_reservas

        self.tela_labs_disponiveis.title('Laboratórios disponíveis')
        self.tela_labs_disponiveis.configure(fg_color='#fff')

        largura = 300
        altura = 575
        x = (self.tela_labs_disponiveis.winfo_screenwidth() - largura) // 2
        y = (self.tela_labs_disponiveis.winfo_screenheight() - altura) // 2
        self.tela_labs_disponiveis.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)
        leaguespartan_font = ctk.CTkFont(family='League Spartan', size=13, weight='bold')
        leaguespartan_font2 = ctk.CTkFont(family='League Spartan', size = 13, weight='normal')

        self.menu_frame = ctk.CTkFrame(tela_labs_disponiveis, fg_color='#274598', height=160, corner_radius=0, width=300)
        self.menu_frame.grid(column=0, row=0)
        self.menu_frame.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        unireservas_logo = ctk.CTkImage(Image.open('imagens/unireservas_logo_branco.png'), size=(170, 51))
        unireservas_logo_lbl = ctk.CTkLabel(self.menu_frame, text="", image=unireservas_logo)
        unireservas_logo_lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font)
        self.suas_reservas_btn.place(rely=0.72, relx=0)

        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff',
                                               fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=150,
                                               height=47, cursor='hand2', font=leaguespartan_font)
        self.novas.place(rely=0.72, relx=0.502)

        self.titulo_frame = ctk.CTkFrame(tela_labs_disponiveis, fg_color='#fff')
        self.titulo_frame.place(relx=0.45, rely=0.35, anchor=tk.CENTER)

        voltar_image = ctk.CTkImage(Image.open('imagens/Back.png'), size=(16, 16))
        voltar_btn = ctk.CTkButton(self.titulo_frame, image=voltar_image, text='', width=25, height=25, fg_color='#fff',
                                   cursor='hand2', hover_color='#fff')
        voltar_btn.grid(column=0, row=0)

        self.salas_disp_lbl = ctk.CTkLabel(self.titulo_frame, text='SALAS DISPONÍVEIS PARA RESERVA:',
                                               text_color='#494949',
                                               font=leaguespartan_font2)
        self.salas_disp_lbl.grid(column=1, row=0, padx=(15, 0))

        self.labs_frame = ctk.CTkScrollableFrame(tela_labs_disponiveis, fg_color='#fff', height=200)
        self.labs_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.lab1_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab1_frame.grid(column=0, row=0, pady=(0, 10))

        self.lab2_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab2_frame.grid(column=0, row=1, pady=(0, 10))

        self.lab3_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab3_frame.grid(column=0, row=2, pady=(0, 10))

        self.lab4_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab4_frame.grid(column=0, row=3, pady=(0, 10))

        self.lab5_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab5_frame.grid(column=0, row=4, pady=(0, 10))

        self.lab6_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab6_frame.grid(column=0, row=5, pady=(0, 10))

        self.lab7_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab7_frame.grid(column=0, row=6, pady=(0, 10))

        self.btn_var = ctk.IntVar()

        self.lab1_btn = ctk.CTkRadioButton(self.lab1_frame, text='Lab 1', text_color='#494949', font=leaguespartan_font2, variable=self.btn_var, value=1, height=35, width=50)
        self.lab1_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab2_btn = ctk.CTkRadioButton(self.lab2_frame, text='Lab 2', text_color='#494949', font=leaguespartan_font2, variable=self.btn_var, value=2, height=35, width=50)
        self.lab2_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab3_btn = ctk.CTkRadioButton(self.lab3_frame, text='Lab 3', text_color='#494949', font=leaguespartan_font2, variable=self.btn_var, value=3, height=35, width=50)
        self.lab3_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab4_btn = ctk.CTkRadioButton(self.lab4_frame, text='Lab 4', text_color='#494949', font=leaguespartan_font2, variable=self.btn_var, value=4, height=35, width=50)
        self.lab4_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab5_btn = ctk.CTkRadioButton(self.lab5_frame, text='Lab 5', text_color='#494949', font=leaguespartan_font2, variable=self.btn_var, value=5, height=35, width=50)
        self.lab5_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab6_btn = ctk.CTkRadioButton(self.lab6_frame, text='Lab 6', text_color='#494949', font=leaguespartan_font2, variable=self.btn_var, value=6, height=35, width=50)
        self.lab6_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab7_btn = ctk.CTkRadioButton(self.lab7_frame, text='Lab 7', text_color='#494949', font=leaguespartan_font2, variable=self.btn_var, value=7, height=35, width=50)
        self.lab7_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.continuar_btn = ctk.CTkButton(tela_labs_disponiveis, text='Continuar', hover_color='#474691', fg_color='#2E2D71', command=self.abrir_tela_reserva_confirmada, corner_radius=20, font=jejugothic_font, height=30, width=200).place(rely=0.86, relx=0.5, anchor=tk.CENTER)

    def abrir_tela_novas_reservas(self):
        from tela_novas_reservas import TelaNovasReservas
        self.tela_labs_disponiveis.withdraw()
        tela_novas_reservas = ctk.CTkToplevel()
        TelaNovasReservas(tela_novas_reservas, self.tela_labs_disponiveis)
        self.tela_labs_disponiveis.wait_window(tela_novas_reservas)

    def voltar_tela_novas_reservas(self):
        self.tela_labs_disponiveis.withdraw()
        self.tela_novas_reservas.deiconify()

    def obter_lab_selecionado(self):
        lab_selecionado = self.btn_var.get()
        return lab_selecionado

    def abrir_tela_reserva_confirmada(self):
        from tela_reserva_confirmada import TelaReservaConfirmada
        self.tela_labs_disponiveis.withdraw()
        tela_reserva_confirmada = ctk.CTkToplevel()
        TelaReservaConfirmada(tela_reserva_confirmada, self.data_selecionada, self.hora_inicio_selecionada, self.hora_fim_selecionada, self.obter_lab_selecionado())
        self.tela_labs_disponiveis.wait_window(tela_reserva_confirmada)
