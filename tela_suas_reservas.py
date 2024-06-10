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

        # Configurações da janela
        self.tela_suas_reservas.title('Suas reservas')
        self.tela_suas_reservas.configure(fg_color='#fff')

        # Definição das dimensões da janela
        largura = 300
        altura = 575
        x = (self.tela_suas_reservas.winfo_screenwidth() - largura) // 2
        y = (self.tela_suas_reservas.winfo_screenheight() - altura) // 2
        self.tela_suas_reservas.geometry(f"{largura}x{altura}+{x}+{y}")

        # Definição das fontes
        leaguespartan_font = ctk.CTkFont(family='League Spartan', size=13, weight='bold')
        leaguespartan_font2 = ctk.CTkFont(family='League Spartan', size=13, weight='normal')
        leaguespartan_font3 = ctk.CTkFont(family='League Spartan', size=12, weight='normal')

        # Frame para o menu
        self.menu_frame = ctk.CTkFrame(tela_suas_reservas, fg_color='#274598', height=160, corner_radius=0, width=300)
        self.menu_frame.grid(column=0, row=0)
        self.menu_frame.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        # Imagem do logotipo
        url = 'https://github.com/marcella2808/UniReservas/blob/master/imagens/unireservas_logo_branco.png?raw=true'
        response = requests.get(url)
        unireservas_logo = ctk.CTkImage(Image.open(BytesIO(response.content)), size=(200, 60))
        unireservas_logo_lbl = ctk.CTkLabel(self.menu_frame, text='', image=unireservas_logo)
        unireservas_logo_lbl.grid(column=0, row=0)
        unireservas_logo_lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        # Botão "Suas Reservas"
        self.suas_reservas_btn = ctk.CTkButton(self.menu_frame, text='Suas reservas', text_color='#fff', fg_color='#1C357B', hover_color='#1C357B', corner_radius=0, width=151, height=47, cursor='hand2', font=leaguespartan_font)
        self.suas_reservas_btn.place(rely=0.72, relx=0)

        # Botão "Novas Reservas"
        self.novas = ctk.CTkButton(self.menu_frame, text='Novas reservas', text_color='#fff', fg_color='#274598', hover_color='#1C357B', corner_radius=0, width=150, height=47, cursor='hand2', font=leaguespartan_font, command=self.abrir_tela_novas_reservas)
        self.novas.place(rely=0.72, relx=0.502)

        # Busca o ID do usuário no banco de dados
        id_usuario = self.banco.buscar_id_usuario(email)
        # Lista as reservas do usuário
        self.reservas = self.banco.listar_reservas_usuario(id_usuario)

        # Verifica o número de reservas para determinar o layout a ser criado
        if 0 < len(self.reservas) < 6:  # Caso a qtde de reservas seja entre 1 e 5, cria um frame normal
            self.reservas_frame = ctk.CTkFrame(tela_suas_reservas, fg_color='#fff', height=200, width=200)
            self.reservas_frame.place(relx=0.5, rely=0.3, anchor='n')

            # Loop sobre as reservas para criar os frames correspondentes
            for reserva in self.reservas:
                self.id_reserva, data, hora_inicio, hora_fim, id_lab = reserva
                reserva_frame = ctk.CTkFrame(self.reservas_frame, fg_color='#f0f0f0', corner_radius=10, width=255, height=40)
                reserva_frame.pack(pady=5, padx=10)

                # Botão para deletar a reserva
                lixeira_icon = ctk.CTkImage(Image.open('imagens/lixeira_icon.png'), size=(17, 17))
                lixeira_icon_btn = ctk.CTkButton(reserva_frame, text='', image=lixeira_icon, fg_color='#f0f0f0', width=30,
                                              height=30, cursor='hand2', hover_color='#ddd', command=lambda id_reserva=self.id_reserva: self.deletar_reserva(id_reserva))
                lixeira_icon_btn.place(relx=0.923, rely=0.5, anchor=tk.CENTER)

                # Informações da reserva
                data_lbl = ctk.CTkLabel(reserva_frame, text=f"Lab {id_lab}    {data}    {hora_inicio} - {hora_fim}",
                                        text_color='#494949', font=leaguespartan_font2)
                data_lbl.place(relx=0.45, rely=0.54, anchor=tk.CENTER)

        elif len(self.reservas) >= 6:  # Caso a qtde de frames seja igual ou maior que 6, cria um frame com scroll
            self.reservas2_frame = ctk.CTkScrollableFrame(tela_suas_reservas, fg_color='#fff', height=300, width=250)
            self.reservas2_frame.place(relx=0.5, rely=0.3, anchor='n')

            # Loop sobre as reservas para criar os frames correspondentes
            for reserva in self.reservas:
                self.id_reserva, data, hora_inicio, hora_fim, id_lab = reserva

                reserva_frame = ctk.CTkFrame(self.reservas2_frame, fg_color='#f0f0f0', corner_radius=10, width=250, height=40)
                reserva_frame.pack(pady=5, padx=10)

                # Botão para deletar a reserva
                lixeira_icon = ctk.CTkImage(Image.open('imagens/lixeira_icon.png'), size=(17, 17))
                lixeira_icon_btn = ctk.CTkButton(reserva_frame, text='', image=lixeira_icon, fg_color='#f0f0f0', width=30,
                                              height=30, cursor='hand2', hover_color='#ddd', command=lambda id_reserva=self.id_reserva: self.deletar_reserva(id_reserva))
                lixeira_icon_btn.place(relx=0.92, rely=0.5, anchor=tk.CENTER)

                # Informações da reserva
                data_lbl = ctk.CTkLabel(reserva_frame, text=f"Lab {id_lab}   {data}   {hora_inicio} - {hora_fim}",
                                        text_color='#494949', font=leaguespartan_font3)
                data_lbl.place(relx=0.45, rely=0.54, anchor=tk.CENTER)

        else:  # Caso não existam reservas ainda, mostra uma mensagem "Não há reservas"
            calendario_img = ctk.CTkImage(Image.open('imagens/calendario_x.png'), size=(200, 200))
            calendario_img_lbl = ctk.CTkLabel(tela_suas_reservas, image=calendario_img, text='')
            calendario_img_lbl.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
            nenhuma_reserva_lbl = ctk.CTkLabel(self.tela_suas_reservas, text='NÃO HÁ RESERVAS', text_color='#151515', font=leaguespartan_font)
            nenhuma_reserva_lbl.place(relx=0.5, rely=0.73, anchor=tk.CENTER)
            nenhuma_reserva_subtitulo_lbl = ctk.CTkLabel(self.tela_suas_reservas, text="Faça um agendamento em 'Novas reservas'", text_color='#444', font=leaguespartan_font3)
            nenhuma_reserva_subtitulo_lbl.place(relx=0.5, rely=0.77, anchor=tk.CENTER)

    def abrir_tela_novas_reservas(self):
        from tela_novas_reservas import TelaNovasReservas # Importa a classe TelaNovasReservas do módulo tela_novas_reservas
        self.tela_suas_reservas.withdraw() # Oculta a janela atual de suas reservas
        tela_novas_reservas = ctk.CTkToplevel() # Cria uma nova janela para as novas reservas
        TelaNovasReservas(tela_novas_reservas, self.tela_suas_reservas, self.banco, self.email) # Inicia a tela de novas reservas com os parâmetros necessários
        self.tela_suas_reservas.wait_window(tela_novas_reservas) # Aguarda até que a janela de novas reservas seja fechada

    def atualizar_tela(self):
        self.tela_suas_reservas.destroy() # Destrói a janela atual de suas reservas
        nova = ctk.CTkToplevel() # Cria uma nova janela de suas reservas
        TelaSuasReservas(nova, self.banco, self.email) # Aguarda até que a nova janela de suas reservas seja fechada
        self.tela_suas_reservas.wait_window(nova)

    def deletar_reserva(self, id_reserva):
        # Exibe uma caixa de diálogo para confirmar a exclusão da reserva
        if messagebox.askokcancel('Deletar reserva', 'Deseja deletar a reserva?'):
            self.banco.deletar_reserva(id_reserva) # Deleta a reserva do banco de dados
            self.atualizar_tela() # Atualiza a tela de suas reservas após a exclusão


