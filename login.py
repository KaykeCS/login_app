import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox as msg, END, StringVar
import sqlite3


class BackEnd():
    def connect_db(self):
        with sqlite3.connect('Sistema.db') as self.conn:
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

    def check_policy_status_checkbox(self):
        checkbox_state = app.policy_status_checkbox_var.get()
        if not checkbox_state:
            msg.showwarning(
                title='Sistema de Cadastro',
                message='Aceite os termos e políticas.'
            )
        else:
            self.registration_user()

    def registration_user(self):

        self.entry_register_username_val = app.entry_register_username.get()
        self.entry_register_email_val = app.entry_register_email.get()
        self.entry_register_password_val = app.entry_register_password.get()
        self.entry_register_cpass_val = app.entry_register_cpass.get()

        try:

            self.connect_db()

            query = """
                INSERT INTO users (Username, Email, Password, ConfPassword)
                VALUES (?, ?, ?, ?)
            """
            data = (self.entry_register_username_val,
                    self.entry_register_email_val,
                    self.entry_register_password_val,
                    self.entry_register_cpass_val)

            with self.conn:
                self.cursor.execute(query, data)

            if (self.entry_register_username_val == '' or
                self.entry_register_email_val == '' or
                self.entry_register_password_val == '' or
                    self.entry_register_cpass_val == ''):
                msg.showerror(
                    title='Sistema de login',
                    message='Erro. \nPreencha todos os campos!')

            elif (len(self.entry_register_username_val) < 4):
                msg.showwarning(
                    title='Sistema de login',
                    message='O Usuário deve conter no mínimo 4 caracteres.'
                )

            elif (len(self.entry_register_password_val) < 4):
                msg.showwarning(
                    title='Sistema de login',
                    message='A Senha deve conter no mínimo 4 caracteres.'
                )

            elif (self.entry_register_password_val !=
                  self.entry_register_cpass_val):
                msg.showerror(
                    title='Sistema de login',
                    message='Erro. \nSenha e Confirmar Senha diferentes.'
                )

            else:
                self.conn.commit()
                msg.showinfo(title='Sistema de login',
                             message='Dados Cadastrados!')

        except sqlite3.Error as e:
            msg.showerror(
                title='Sistema de login',
                message=f"Erro ao inserir dados: {str(e)}")

        finally:

            app.clean_entry_register()
            self.disconnect_db()

    def check_remember_status_checkbox(self):
        remember_checkbox_state = app.remember_status_checkbox_var.get()

        if remember_checkbox_state == 'off':
            self.login_verify()

        else:
            print('marcada')

    def login_verify(self):

        self.connect_db()
        self.login_username = app.entry_login_username.get()
        self.login_password = app.entry_login_password.get()
        self.cursor.execute(
            """SELECT * FROM users WHERE (Username = ? AND Password = ?)""",
            (self.login_username, self.login_password))
        self.check_data = self.cursor.fetchone()

        try:
            if (self.login_username == '' or self.login_password == ''):
                msg.showwarning(
                    title='Sistema de login',
                    message='Preencha todos os campos.')

            elif (self.login_username
                  in self.check_data and self.login_password
                    in self.check_data):
                msg.showinfo(
                    title='Sistema de Login',
                    message='Logando...')
                app.clean_entry_login()

        except:
            msg.showerror(
                title='Sistema de login',
                message='Erro. Verifique seu login e senha novamente.')
            self.disconnect_db()


class Application(BackEnd):
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        self.window_root()
        self.remember_status_checkbox_var = tk.StringVar()
        self.login()
        self.policy_status_checkbox_var = tk.StringVar()

    def window_root(self):
        self.root.geometry('700x400')
        self.root.title('Sistema de login')
        self.root.iconbitmap('icon.ico')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.root.resizable(False, False)

    def login(self):
        self.login_frame = ctk.CTkFrame(
            master=self.root, width=350, height=396)
        self.login_frame.pack()

        label = ctk.CTkLabel(master=self.login_frame,
                             text='Sistema de Login',
                             font=('Roboto', 30))
        label.place(x=35, y=25)

        self.entry_login_username = ctk.CTkEntry(
            master=self.login_frame,
            placeholder_text='Nome de Usuário',
            width=300,
            font=("Arial", 16)
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
            font=("Arial", 16),
            show='*'
        )
        self.entry_login_password.place(x=25, y=175)

        password_label2 = ctk.CTkLabel(
            master=self.login_frame,
            text='*Esse campo exige caracter obrigatório.',
            text_color='green'
        )
        password_label2.place(x=25, y=205)

        self.remember_checkbox = ctk.CTkCheckBox(
            master=self.login_frame,
            text='Lembrar-se de mim sempre',
            command=self.remember_checkbox_event,
            variable=self.remember_status_checkbox_var,
            onvalue="on",
            offvalue="off"
        )
        self.remember_checkbox.place(x=25, y=235)

        login_button = ctk.CTkButton(
            master=self.login_frame,
            text='Login',
            width=300,
            command=self.check_remember_status_checkbox
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

    def back_button(self):
        self.register_frame.pack_forget()
        self.login_frame.pack()

    def save_user(self):
        self.msg_save = msg.showinfo(
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

        self.checkbox_policy = ctk.CTkCheckBox(
            master=self.register_frame,
            text='Aceito todos os Termos e Políticas',
            command=self.checkbox_event,
            variable=self.policy_status_checkbox_var,
            onvalue="on",
            offvalue="off"
        )

        self.checkbox_policy.place(x=25, y=265)

        back_button = ctk.CTkButton(master=self.register_frame,
                                    text='VOLTAR',
                                    width=145,
                                    fg_color='gray',
                                    hover_color='#202020',
                                    command=self.back_button)
        back_button.place(x=25, y=315)

        save_button = ctk.CTkButton(
            master=self.register_frame,
            text='Cadastrar',
            width=145,
            fg_color='green',
            hover_color='#014B05',
            command=self.check_policy_status_checkbox
        )
        save_button.place(x=180, y=315)

    def checkbox_event(self):
        print("checkbox toggled, current value:",
              self.policy_status_checkbox_var.get())

    def remember_checkbox_event(self):
        print("checkbox toggled, current value:",
              self.remember_status_checkbox_var.get())

    def clean_entry_register(self):
        self.entry_register_username.delete(0, END)
        self.entry_register_email.delete(0, END)
        self.entry_register_password.delete(0, END)
        self.entry_register_cpass.delete(0, END)

    def clean_entry_login(self):
        self.entry_login_username.delete(0, END)
        self.entry_login_password.delete(0, END)


if __name__ == "__main__":
    app = Application()
    app.root.mainloop()
