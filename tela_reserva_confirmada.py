import tkinter as tk
from io import BytesIO

import customtkinter as ctk
import requests
from PIL import Image
from tkinter import messagebox


class TelaReservaConfirmada:
    def __init__(self, tela_reserva_confirmada, data_selecionada, hora_inicio_selecionada, hora_fim_selecionada, lab_selecionado, tela_labs_disponiveis, banco, email):
        self.tela_reserva_confirmada = tela_reserva_confirmada
        self.data_selecionada = data_selecionada
        self.hora_inicio_selecionada = hora_inicio_selecionada
        self.hora_fim_selecionada = hora_fim_selecionada
        self.lab_selecionado = lab_selecionado
        self.tela_labs_disponiveis = tela_labs_disponiveis
        self.banco = banco
        self.email = email

        # Configurações da janela
        self.tela_reserva_confirmada.title('Confirmação de reserva')
        self.tela_reserva_confirmada.configure(fg_color='#fff')

        largura = 300
        altura = 575
        x = (self.tela_reserva_confirmada.winfo_screenwidth() - largura) // 2
        y = (self.tela_reserva_confirmada.winfo_screenheight() - altura) // 2
        self.tela_reserva_confirmada.geometry(f"{largura}x{altura}+{x}+{y}")

        # Configurações da janela
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)
        leaguespartan_font1 = ctk.CTkFont(family='League Spartan', size=13, weight='bold')
        leaguespartan_font2 = ctk.CTkFont(family='League Spartan', size=13, weight='normal')

        # Frame do menu
        self.menu_frame = ctk.CTkFrame(tela_reserva_confirmada, fg_color='#274598', height=160, corner_radius=0, width=300)
        self.menu_frame.grid(column=0, row=0)
        self.menu_frame.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        # Logotipo
        url = 'https://github.com/marcella2808/UniReservas/blob/master/imagens/unireservas_logo_branco.png?raw=true'
        response = requests.get(url)
        unireservas_logo = ctk.CTkImage(Image.open(BytesIO(response.content)), size=(200, 60))
        unireservas_logo_lbl = ctk.CTkLabel(self.menu_frame, text='', image=unireservas_logo)
        unireservas_logo_lbl.grid(column=0, row=0)
        unireservas_logo_lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        # Botões do menu
        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font1, command=self.abrir_tela_suas_reservas)
        self.suas_reservas_btn.place(rely=0.72, relx=0)

        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff',
                                               fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=150,
                                               height=47, cursor='hand2', font=leaguespartan_font1)
        self.novas.place(rely=0.72, relx=0.502)

        # Frame do título
        self.titulo_frame = ctk.CTkFrame(tela_reserva_confirmada, fg_color='#fff')
        self.titulo_frame.place(relx=0.4, rely=0.35, anchor=tk.CENTER)

        # Botão de voltar
        voltar_image = ctk.CTkImage(Image.open('imagens/voltar_icon.png'), size=(16, 16))
        voltar_btn = ctk.CTkButton(self.titulo_frame, image=voltar_image, text='', width=25, height=25, fg_color='#fff', cursor='hand2', hover_color='#fff', command=self.voltar_tela_labs_disponiveis)
        voltar_btn.grid(column=0, row=0)

        # Label do título
        self.reserva_confirmada_lbl = ctk.CTkLabel(self.titulo_frame, text='CONFIRMAR RESERVA', font=leaguespartan_font2, text_color='#494949')
        self.reserva_confirmada_lbl.grid(column=1, row=0, padx=(35, 0))

        # Frame das informações
        self.infos_frame = ctk.CTkFrame(tela_reserva_confirmada, width=210, height=140, fg_color='#AFB1D1', border_color='#38529F', border_width=1)
        self.infos_frame.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        # Labels das informações da reserva
        self.data_lbl = ctk.CTkLabel(self.infos_frame, text='DATA: ' + self.data_selecionada, text_color='#494949', fg_color='#f0f0f0', width=160, corner_radius=7, font=leaguespartan_font2)
        self.data_lbl.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.horario_lbl = ctk.CTkLabel(self.infos_frame, text='HORÁRIO: ' + self.hora_inicio_selecionada + ' - ' + self.hora_fim_selecionada, text_color='#494949', fg_color='#f0f0f0',
                                     width=160, corner_radius=7, font=leaguespartan_font2)
        self.horario_lbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lab_lbl = ctk.CTkLabel(self.infos_frame, text='LAB ' + str(self.lab_selecionado), text_color='#494949', fg_color='#f0f0f0',
                                        width=160, corner_radius=7, font=leaguespartan_font2)
        self.lab_lbl.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

        # Botão de confirmação
        self.confirmar_btn = ctk.CTkButton(tela_reserva_confirmada, text='Confirmar', hover_color='#474691', fg_color='#2E2D71', corner_radius=20, font=jejugothic_font, height=30, width=200, command=self.confirmar_reserva, cursor='hand2').place(
            rely=0.8, relx=0.5, anchor=tk.CENTER)

    def abrir_tela_suas_reservas(self):
        from tela_suas_reservas import TelaSuasReservas
        self.tela_reserva_confirmada.withdraw() # Esconde a janela atual
        tela_suas_reservas = ctk.CTkToplevel() # Cria uma nova janela
        TelaSuasReservas(tela_suas_reservas, self.banco, self.email) # Inicializa a tela de suas reservas
        self.tela_reserva_confirmada.wait_window(tela_suas_reservas) # Aguarda o fechamento da nova janela

    def voltar_tela_labs_disponiveis(self):
        self.tela_reserva_confirmada.withdraw() # Esconde a janela atual
        self.tela_labs_disponiveis.deiconify() # Exibe a tela de laboratórios disponíveis

    def confirmar_reserva(self):
        email_usuario = self.email # Obtém o email do usuário
        id_usuario = self.banco.buscar_id_usuario(email_usuario) # Busca o ID do usuário no banco de dados
        id_laboratorio = self.banco.buscar_id_laboratorio("Lab " + str(self.lab_selecionado)) # Busca o ID do laboratório selecionado no banco de dados

        # Verifica se o ID do usuário e do laboratório foram encontrados
        if id_usuario is not None and id_laboratorio is not None:
            # Adiciona a reserva no banco de dados
            self.banco.adicionar_reserva(id_usuario, id_laboratorio, self.data_selecionada,
                                         self.hora_inicio_selecionada, self.hora_fim_selecionada)
            # Exibe uma mensagem de confirmação
            messagebox.showinfo('Confirmação de reserva', 'Reserva confirmada com sucesso!')
            self.abrir_tela_suas_reservas() # Abre a tela de suas reservas
        else:
            # Exibe uma mensagem de erro caso os dados não tenham sido encontrados no banco
            messagebox.showerror('Erro',
                                 'Não foi possível confirmar a reserva. Verifique os dados e tente novamente.')
