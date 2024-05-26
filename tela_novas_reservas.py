import tkinter as tk
from io import BytesIO
from tkinter import ttk, messagebox
import customtkinter as ctk
import requests
from PIL import Image
from tkcalendar import Calendar
from datetime import datetime
from datetime import date


class TelaNovasReservas:
    def __init__(self, tela_novas_reservas, tela_suas_reservas, banco):
        self.tela_novas_reservas = tela_novas_reservas
        self.tela_suas_reservas = tela_suas_reservas
        self.banco = banco
        self.tela_novas_reservas.title('Novas reservas')
        self.tela_novas_reservas.configure(fg_color='#fff')

        largura = 300
        altura = 575
        x = (self.tela_novas_reservas.winfo_screenwidth() - largura) // 2
        y = (self.tela_novas_reservas.winfo_screenheight() - altura) // 2
        self.tela_novas_reservas.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        inter_font = ctk.CTkFont(family='Inter', size=16)
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)
        leaguespartan_font1 = ctk.CTkFont(family='League Spartan', size=13, weight='bold')
        leaguespartan_font2 = ctk.CTkFont(family='League Spartan', size=13, weight='normal')
        leaguespartan_font3 = ctk.CTkFont(family='League Spartan', size=18, weight='normal')

        self.menu_frame = ctk.CTkFrame(tela_novas_reservas, fg_color='#274598', height=160, corner_radius=0, width=300)
        self.menu_frame.grid(column=0, row=0)
        self.menu_frame.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        url = 'https://github.com/marcella2808/UniReservas/blob/master/imagens/unireservas_logo_branco.png?raw=true'
        response = requests.get(url)
        unireservas_logo = ctk.CTkImage(Image.open(BytesIO(response.content)), size=(200, 60))
        unireservas_logo_lbl = ctk.CTkLabel(self.menu_frame, text='', image=unireservas_logo)
        unireservas_logo_lbl.grid(column=0, row=0)
        unireservas_logo_lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font1, command=self.voltar_tela_suas_reservas)
        self.suas_reservas_btn.place(rely=0.72, relx=0)

        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff',
                                               fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=150,
                                               height=47, cursor='hand2', font=leaguespartan_font1)
        self.novas.place(rely=0.72, relx=0.502)

        self.calendario_frame = ctk.CTkFrame(tela_novas_reservas, fg_color='#fff')
        self.calendario_frame.place(relx=0.5, rely=0.59, anchor=tk.CENTER)

        self.selecione_data_lbl = ctk.CTkLabel(self.calendario_frame, text='SELECIONE A DATA DA RESERVA:', text_color='#484848',
                                               font=leaguespartan_font2)
        self.selecione_data_lbl.grid(column=0, row=0, pady=(0, 15))

        self.data_hoje = datetime.now()
        self.calendario = Calendar(self.calendario_frame, font=inter_font, cursor='hand2', mindate=self.data_hoje, showweeknumbers=False, locale='pt_BR', date_pattern='dd/mm/yyyy', firstweekday='sunday', background='#274598', foreground='white', headersbackground='white', headersforeground='#666', selectbackground='#274598', normalbackground='white', weekendbackground='white', normalforeground='#333', weekendforeground='#333', othermonthbackground='white', othermonthforeground='#aaa', othermonthwebackground='white', othermonthweforeground='#aaa', bordercolor='#e0e0e0')
        self.calendario.grid(column=0, row=1)

        self.data_selecionada_lbl = ctk.CTkLabel(self.calendario_frame, text=str(date.today().strftime('%d/%m/%Y')),
                                                 text_color='#484848',
                                                 font=leaguespartan_font2, bg_color='#ebebeb', padx=10, pady=10)
        self.data_selecionada_lbl.grid(column=0, row=2, pady=(10, 0))
        self.calendario.bind("<<CalendarSelected>>", self.mostrar_data_selecionada)

        self.horario_frame = ctk.CTkFrame(self.calendario_frame, fg_color='#fff')
        self.horario_frame.grid(column=0, row=3, pady=(15, 0))

        self.hora_inicio_lbl = ctk.CTkLabel(self.horario_frame, text='DE', text_color='#484848', font=leaguespartan_font2)
        self.hora_inicio_lbl.grid(column=0, row=1)

        self.hora_fim_lbl = ctk.CTkLabel(self.horario_frame, text='ATÉ', text_color='#484848', font=leaguespartan_font2)
        self.hora_fim_lbl.grid(column=2, row=1)

        horas = ["06:00", "06:15", "06:30", "06:45", "07:00", "07:15", "07:30", "07:45", "08:00", "08:15",
         "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45",
         "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15",
         "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45",
         "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15",
         "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45",
         "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00"]

        horas_ordenadas = sorted(horas)

        self.hora_inicio_entry = ttk.Combobox(self.horario_frame, values=horas_ordenadas, font=leaguespartan_font3, width=5)
        self.hora_inicio_entry.grid(column=0, row=2)

        self.as_lbl = ctk.CTkLabel(self.horario_frame, text='ÀS', text_color='#484848', font=leaguespartan_font2)
        self.as_lbl.grid(column=1, row=2, padx=15)

        self.hora_fim_entry = ttk.Combobox(self.horario_frame, values=horas_ordenadas, font=leaguespartan_font3, width=5)
        self.hora_fim_entry.grid(column=2, row=2)

        self.continuar_btn = ctk.CTkButton(self.calendario_frame, text='Continuar', text_color='#fff',
                                           hover_color='#474691', fg_color='#2E2D71', cursor='hand2',
                                           corner_radius=20, font=jejugothic_font, height=30, width=200, command=self.continuar)
        self.continuar_btn.grid(column=0, row=4, pady=(20, 0))

    def voltar_tela_suas_reservas(self):
        self.tela_novas_reservas.withdraw()
        self.tela_suas_reservas.deiconify()

    def validar_horarios(self):
        # Obtém os horários selecionados pelo usuário
        hora_inicio = self.hora_inicio_entry.get()
        hora_fim = self.hora_fim_entry.get()

        # Converte os horários para inteiros para facilitar a comparação
        hora_inicio_int = int(hora_inicio.replace(':', ''))
        hora_fim_int = int(hora_fim.replace(':', ''))

        # Verifica se o primeiro horário é anterior ao segundo
        if hora_inicio_int >= hora_fim_int:
            return False
        else:
            return True

    def abrir_tela_labs_disponiveis(self):
        from tela_labs_disponiveis import TelaLabsDisponiveis
        self.tela_novas_reservas.withdraw()
        tela_labs_disponiveis = ctk.CTkToplevel()
        data_selecionada = self.calendario.get_date()
        hora_inicio = self.hora_inicio_entry.get()
        hora_fim = self.hora_fim_entry.get()
        TelaLabsDisponiveis(tela_labs_disponiveis, data_selecionada, hora_inicio, hora_fim, self.tela_novas_reservas, self.banco)
        self.tela_novas_reservas.wait_window(tela_labs_disponiveis)

    def continuar(self):
        if not self.validar_horarios():
            messagebox.showerror('Novas reservas', 'Selecione um intervalo de tempo válido.')
        else:
            self.abrir_tela_labs_disponiveis()

    def mostrar_data_selecionada(self, event=None):
        data_selecionada = self.calendario.get_date()
        self.data_selecionada_lbl.configure(text=data_selecionada)

