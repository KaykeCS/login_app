import customtkinter as ctk
import tkinter as tk
root = ctk.CTk()


class Application():
    def __init__(self):
        self.root = ctk.CTk()
        self.theme()
        self.screen()
        self.login()
        self.root.mainloop()

    def theme(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def screen(self):
        self.root.geometry('700x400')
        self.root.title('Sistema de login')
        self.root.iconbitmap('icon.ico')
        self.root.resizable(False, False)

    def login(self):
        login_frame = ctk.CTkFrame(master=self.root, width=350, height=396)
        login_frame.pack()

        label = ctk.CTkLabel(master=login_frame,
                             text='Sistema de login',
                             font=('Roboto', 20))
        label.place(x=25, y=5)
        username_entry1 = ctk.CTkEntry(
            master=login_frame,
            placeholder_text='Nome de Usuário',
            width=300,
            font=("Arial", 10)
        )
        username_entry1.place(x=25, y=105)

        username_label1 = ctk.CTkLabel(
            master=login_frame,
            text='*Esse campo exige caracter obrigatório.',
            text_color='green'
        )
        username_label1.place(x=25, y=135)

        password_entry2 = ctk.CTkEntry(
            master=login_frame,
            placeholder_text='Senha',
            width=300,
            font=("Arial", 10),
            show='*'
        )
        password_entry2.place(x=25, y=175)

        password_label2 = ctk.CTkLabel(
            master=login_frame,
            text='*Esse campo exige caracter obrigatório.',
            text_color='green'
        )
        password_label2.place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(
            master=login_frame,
            text='Lembrar-se de mim sempre'
        )
        checkbox.place(x=25, y=235)

        login_button = ctk.CTkButton(
            master=login_frame,
            text='Login',
            width=300
        )
        login_button.place(x=25, y=285)

        register_span = ctk.CTkLabel(
            master=login_frame,
            text='Não possui uma conta ?'
        )
        register_span.place(x=25, y=325)

        register_button = ctk.CTkButton(
            master=login_frame,
            text='Cadastre-se',
            width=150,
            fg_color='green',
            hover_color='#2D9334'
        )
        register_button.place(x=175, y=325)


Application()
