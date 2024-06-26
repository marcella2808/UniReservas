import tkinter as tk
from io import BytesIO
from tkinter import messagebox

import customtkinter as ctk
import requests
from PIL import Image


class TelaLabsDisponiveis:
    def __init__(self, tela_labs_disponiveis, data_selecionada, hora_inicio_selecionada, hora_fim_selecionada, tela_novas_reservas, banco, email):
        self.tela_labs_disponiveis = tela_labs_disponiveis
        self.data_selecionada = data_selecionada
        self.hora_inicio_selecionada = hora_inicio_selecionada
        self.hora_fim_selecionada = hora_fim_selecionada
        self.tela_novas_reservas = tela_novas_reservas
        self.banco = banco
        self.email = email

        # Configurações iniciais da janela
        self.tela_labs_disponiveis.title('Laboratórios disponíveis')
        self.tela_labs_disponiveis.configure(fg_color='#fff')

        # Dimensões e posição da janela
        largura = 300
        altura = 575
        x = (self.tela_labs_disponiveis.winfo_screenwidth() - largura) // 2
        y = (self.tela_labs_disponiveis.winfo_screenheight() - altura) // 2
        self.tela_labs_disponiveis.geometry(f"{largura}x{altura}+{x}+{y}")

        # fontes
        jejugothic_font = ctk.CTkFont(family='JejuGothic', size=12)
        leaguespartan_font = ctk.CTkFont(family='League Spartan', size=13, weight='bold')
        leaguespartan_font2 = ctk.CTkFont(family='League Spartan', size = 13, weight='normal')

        # Configuração das fontes
        self.menu_frame = ctk.CTkFrame(tela_labs_disponiveis, fg_color='#274598', height=160, corner_radius=0, width=300)
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
        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font)
        self.suas_reservas_btn.place(rely=0.72, relx=0)
        
        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff',
                                               fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=150,
                                               height=47, cursor='hand2', font=leaguespartan_font)
        self.novas.place(rely=0.72, relx=0.502)

        # Frame do título
        self.titulo_frame = ctk.CTkFrame(tela_labs_disponiveis, fg_color='#fff')
        self.titulo_frame.place(relx=0.45, rely=0.35, anchor=tk.CENTER)

        # Botão de voltar
        voltar_image = ctk.CTkImage(Image.open('imagens/voltar_icon.png'), size=(16, 16))
        voltar_btn = ctk.CTkButton(self.titulo_frame, image=voltar_image, text='', width=25, height=25, fg_color='#fff',
                                   cursor='hand2', hover_color='#fff', command=self.voltar_tela_novas_reservas)
        voltar_btn.grid(column=0, row=0)

        # Legenda "Salas Disponíveis"
        self.salas_disp_lbl = ctk.CTkLabel(self.titulo_frame, text='SALAS DISPONÍVEIS PARA RESERVA:',
                                               text_color='#494949',
                                               font=leaguespartan_font2)
        self.salas_disp_lbl.grid(column=1, row=0, padx=(15, 0))

        # Frame rolável para as opções de laboratórios
        self.labs_frame = ctk.CTkScrollableFrame(tela_labs_disponiveis, fg_color='#fff', height=200)
        self.labs_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Frames para cada laboratório
        self.lab1_frame = ctk.CTkFrame(self.labs_frame, fg_color='#f0f0f0', width=200, height=35, corner_radius=10)
        self.lab1_frame.grid(column=0, row=0, pady=(0, 10))

        # Frames para cada laboratório
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

        self.btn_var = ctk.IntVar() # Variável para armazenar o valor do botão selecionado
        
        # Botões de seleção de laboratórios
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

        self.continuar_btn = ctk.CTkButton(tela_labs_disponiveis, text='Continuar', hover_color='#474691', fg_color='#2E2D71', command=self.abrir_tela_reserva_confirmada, corner_radius=20, font=jejugothic_font, height=30, width=200, cursor='hand2').place(rely=0.86, relx=0.5, anchor=tk.CENTER)

    def abrir_tela_novas_reservas(self):  # Função para abrir a tela de novas reservas
        from tela_novas_reservas import TelaNovasReservas # Importa a classe TelaNovasReservas do módulo tela_novas_reservas
        self.tela_labs_disponiveis.withdraw() # Oculta a tela atual de laboratórios disponíveis
        tela_novas_reservas = ctk.CTkToplevel() # Cria uma nova janela CTkToplevel para a tela de novas reservas
        TelaNovasReservas(tela_novas_reservas, self.tela_labs_disponiveis, self.email) # Inicializa a tela de novas reservas com a nova janela, a tela atual e o email do usuário
        self.tela_labs_disponiveis.wait_window(tela_novas_reservas) # Aguarda o fechamento da nova janela antes de continuar

    def voltar_tela_novas_reservas(self): # Função para voltar à tela de novas reservas
        self.tela_labs_disponiveis.withdraw()
        self.tela_novas_reservas.deiconify()

    def obter_lab_selecionado(self): # Função para obter o laboratório selecionado
        lab_selecionado = self.btn_var.get() # Obtém o valor do botão de seleção de laboratório
        return lab_selecionado # Retorna o laboratório selecionado

    def abrir_tela_reserva_confirmada(self): # Função para abrir a tela de confirmação de reserva
        if self.btn_var.get() == 0: # Verifica se nenhum laboratório foi selecionado
            messagebox.showerror('Erro',
                                 'Selecione um laboratório.') # Exibe uma mensagem de erro solicitando a seleção de um laboratório
        else: # Importa a classe TelaReservaConfirmada do módulo tela_reserva_confirmada
            from tela_reserva_confirmada import TelaReservaConfirmada
            self.tela_labs_disponiveis.withdraw() # Oculta a tela atual de laboratórios disponíveis
            tela_reserva_confirmada = ctk.CTkToplevel() # Cria uma nova janela CTkToplevel para a tela de confirmação de reserva
            TelaReservaConfirmada(tela_reserva_confirmada, self.data_selecionada, self.hora_inicio_selecionada, self.hora_fim_selecionada, self.obter_lab_selecionado(), self.tela_labs_disponiveis, self.banco, self.email)
            self.tela_labs_disponiveis.wait_window(tela_reserva_confirmada) # Aguarda o fechamento da nova janela antes de continuar
