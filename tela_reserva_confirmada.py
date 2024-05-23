import tkinter as tk
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox


class TelaReservaConfirmada:
    def __init__(self, tela_reserva_confirmada, data_selecionada, hora_inicio_selecionada, hora_fim_selecionada, lab_selecionado):
        self.tela_reserva_confirmada = tela_reserva_confirmada
        self.data_selecionada = data_selecionada
        self.hora_inicio_selecionada = hora_inicio_selecionada
        self.hora_fim_selecionada = hora_fim_selecionada
        self.lab_selecionado = lab_selecionado

        self.tela_reserva_confirmada.title('Confirmação de reserva')
        self.tela_reserva_confirmada.configure(fg_color='#fff')

        largura = 300
        altura = 575
        x = (self.tela_reserva_confirmada.winfo_screenwidth() - largura) // 2
        y = (self.tela_reserva_confirmada.winfo_screenheight() - altura) // 2
        self.tela_reserva_confirmada.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)
        leaguespartan_font1 = ctk.CTkFont(family='League Spartan', size=13, weight='bold')
        leaguespartan_font2 = ctk.CTkFont(family='League Spartan', size=13, weight='normal')

        self.menu_frame = ctk.CTkFrame(tela_reserva_confirmada, fg_color='#274598', height=160, corner_radius=0, width=300)
        self.menu_frame.grid(column=0, row=0)
        self.menu_frame.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        unireservas_logo = ctk.CTkImage(Image.open('imagens/unireservas_logo_branco.png'), size=(170, 51))
        unireservas_logo_lbl = ctk.CTkLabel(self.menu_frame, text='', image=unireservas_logo)
        unireservas_logo_lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font1, command=self.abrir_tela_suas_reservas)
        self.suas_reservas_btn.place(rely=0.72, relx=0)

        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff',
                                               fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=150,
                                               height=47, cursor='hand2', font=leaguespartan_font1)
        self.novas.place(rely=0.72, relx=0.502)

        self.titulo_frame = ctk.CTkFrame(tela_reserva_confirmada, fg_color='#fff')
        self.titulo_frame.place(relx=0.4, rely=0.35, anchor=tk.CENTER)

        voltar_image = ctk.CTkImage(Image.open('imagens/Back.png'), size=(16, 16))
        voltar_btn = ctk.CTkButton(self.titulo_frame, image=voltar_image, text='', width=25, height=25, fg_color='#fff', cursor='hand2', hover_color='#fff')
        voltar_btn.grid(column=0, row=0)

        self.reserva_confirmada_lbl = ctk.CTkLabel(self.titulo_frame, text='CONFIRMAR RESERVA', font=leaguespartan_font2, text_color='#494949')
        self.reserva_confirmada_lbl.grid(column=1, row=0, padx=(35, 0))

        self.infos_frame = ctk.CTkFrame(tela_reserva_confirmada, width=210, height=140, fg_color='#AFB1D1', border_color='#38529F', border_width=1)
        self.infos_frame.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        self.data_lbl = ctk.CTkLabel(self.infos_frame, text='DATA: ' + self.data_selecionada, text_color='#494949', fg_color='#f0f0f0', width=160, corner_radius=7, font=leaguespartan_font2)
        self.data_lbl.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.horario_lbl = ctk.CTkLabel(self.infos_frame, text='HORÁRIO: ' + self.hora_inicio_selecionada + ' - ' + self.hora_fim_selecionada, text_color='#494949', fg_color='#f0f0f0',
                                     width=160, corner_radius=7, font=leaguespartan_font2)
        self.horario_lbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab_lbl = ctk.CTkLabel(self.infos_frame, text='LAB ' + str(self.lab_selecionado), text_color='#494949', fg_color='#f0f0f0',
                                        width=160, corner_radius=7, font=leaguespartan_font2)
        self.lab_lbl.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

        self.confirmar_btn = ctk.CTkButton(tela_reserva_confirmada, text='Confirmar', hover_color='#474691', fg_color='#2E2D71', corner_radius=20, font=jejugothic_font, height=30, width=200, command=self.confirmar_reserva).place(
            rely=0.8, relx=0.5, anchor=tk.CENTER)

    def abrir_tela_suas_reservas(self):
        from tela_suas_reservas import TelaSuasReservas
        self.tela_reserva_confirmada.withdraw()
        tela_suas_reservas = ctk.CTkToplevel()
        TelaSuasReservas(tela_suas_reservas)
        self.tela_reserva_confirmada.wait_window(tela_suas_reservas)

    def voltar_tela_labs_disponiveis(self):
        pass

    def confirmar_reserva(self):
        messagebox.showinfo('Confirmação de reserva', 'Reserva confirmada com sucesso!')


