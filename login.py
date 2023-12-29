import customtkinter as ctk
from tkinter import messagebox, END
import sqlite3


class Application():
    def __init__(self):
        self.root = ctk.CTk()
        self.theme()
        self.window_root()
        self.login()

    def theme(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def window_root(self):
        self.root.geometry('700x400')
        self.root.title('Sistema de login')
        self.root.iconbitmap('icon.ico')
        self.root.resizable(False, False)

    def message_box_login(self):
        self.msg = messagebox.showinfo(
            title='Status de Login',
            message='Login Feito com Sucesso!')

    def login(self):
        self.login_frame = ctk.CTkFrame(
            master=self.root, width=350, height=396)
        self.login_frame.pack()

        label = ctk.CTkLabel(master=self.login_frame,
                             text='Sistema de login',
                             font=('Roboto', 20))
        label.place(x=25, y=5)

        self.entry_login_username = ctk.CTkEntry(
            master=self.login_frame,
            placeholder_text='Nome de Usuário',
            width=300,
            font=("Arial", 10)
        )
        self.entry_login_username.place(x=25, y=105)

        username_label1 = ctk.CTkLabel(
            master=self.login_frame,
            text='*Esse campo exige caracter obrigatório.',
            text_color='green'
        )
        username_label1.place(x=25, y=135)

        self.entry_login_password = ctk.CTkEntry(
            master=self.login_frame,
            placeholder_text='Senha',
            width=300,
            font=("Arial", 10),
            show='*'
        )
        self.entry_login_password.place(x=25, y=175)

        password_label2 = ctk.CTkLabel(
            master=self.login_frame,
            text='*Esse campo exige caracter obrigatório.',
            text_color='green'
        )
        password_label2.place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(
            master=self.login_frame,
            text='Lembrar-se de mim sempre'
        )
        checkbox.place(x=25, y=235)

        login_button = ctk.CTkButton(
            master=self.login_frame,
            text='Login',
            width=300,
            command=self.message_box_login
        )
        login_button.place(x=25, y=285)

        register_span = ctk.CTkLabel(
            master=self.login_frame,
            text='Não possui uma conta ?'
        )
        register_span.place(x=25, y=325)

        self.register_button = ctk.CTkButton(
            master=self.login_frame,
            text='Cadastre-se',
            width=150,
            fg_color='green',
            hover_color='#2D9334',
            command=self.registration_screen)
        self.register_button.place(x=175, y=325)

    def back(self):
        self.register_frame.pack_forget()
        self.login_frame.pack()

    def save_user(self):
        self.msg_save = messagebox.showinfo(
            title='Status do Cadastro', message='Cadastro Efetuado.')

    def registration_screen(self):
        self.login_frame.pack_forget()

        self.register_frame = ctk.CTkFrame(
            master=self.root,
            width=350,
            height=396)
        self.register_frame.pack()

        self.register_label = ctk.CTkLabel(
            master=self.register_frame,
            text="Crie a sua Conta",
            font=("Roboto", 20))
        self.register_label.place(x=25, y=5)

        span = ctk.CTkLabel(master=self.register_frame,
                            text='Preencha todos os campos corretamente.',
                            font=('Roboto', 11),
                            text_color='gray')
        span.place(x=25, y=65)

        self.entry_register_username = ctk.CTkEntry(
            master=self.register_frame,
            placeholder_text='Nome de Usuário',
            width=300,
            font=("Arial", 13)
        )
        self.entry_register_username.place(x=25, y=105)

        self.entry_register_email = ctk.CTkEntry(
            master=self.register_frame,
            placeholder_text='E-mail de Usuário',
            width=300,
            font=("Arial", 13)
        )
        self.entry_register_email.place(x=25, y=145)

        self.entry_register_password = ctk.CTkEntry(
            master=self.register_frame,
            placeholder_text='Senha de Usuário',
            width=300,
            font=("Arial", 13),
            show='*'
        )
        self.entry_register_password.place(x=25, y=185)

        self.entry_register_cpass = ctk.CTkEntry(
            master=self.register_frame,
            placeholder_text='Confirmar senha',
            width=300,
            font=("Arial", 13),
            show='*'
        )

        self.entry_register_cpass.place(x=25, y=225)

        checkbox = ctk.CTkCheckBox(
            master=self.register_frame,
            text='Aceito todos os Termos e Políticas'
        )
        checkbox.place(x=25, y=265)

        back_button = ctk.CTkButton(master=self.register_frame,
                                    text='VOLTAR',
                                    width=145,
                                    fg_color='gray',
                                    hover_color='#202020',
                                    command=self.back)
        back_button.place(x=25, y=315)

        save_button = ctk.CTkButton(
            master=self.register_frame,
            text='Cadastrar',
            width=145,
            fg_color='green',
            hover_color='#014B05',
            command=backend.registration_user
        )
        save_button.place(x=180, y=315)

    def clean_entry_register(self):
        self.entry_register_username.delete(0, END)
        self.entry_register_email.delete(0, END)
        self.entry_register_password.delete(0, END)
        self.entry_register_cpass.delete(0, END)

    def clean_entry_login(self):
        self.entry_login_username.delete(0, END)
        self.entry_login_password.delete(0, END)


class BackEnd():
    def connect_db(self):
        self.conn = sqlite3.connect("Sistema.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado.")

    def disconnect_db(self):
        self.conn.close()
        print("Banco de dados desconectado.")

    def create_table(self):
        self.connect_db()
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Username TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Password TEXT NOT NULL,
                    ConfPassword TEXT NOT NULL
)""")
        self.conn.commit()
        print("Tabela criada.")
        self.disconnect_db()

    def registration_user(self, ):
        entry_register_username = app.entry_register_username.get()
        entry_register_email = app.entry_register_email.get()
        entry_register_password = app.entry_register_password.get()
        entry_register_cpass = app.entry_register_cpass.get()
        print(entry_register_username,
              entry_register_email,
              entry_register_password,
              entry_register_cpass)


if __name__ == "__main__":
    app = Application()
    backend = BackEnd()
    app.root.mainloop()
