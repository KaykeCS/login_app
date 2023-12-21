import customtkinter
import tkinter
from tkinter import RIGHT

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.geometry('700x400')
window.title('Sistema de login')
window.iconbitmap('icon.ico')
window.resizable(False, False)

# tela
img = tkinter.PhotoImage(file='log.png')
label_img = customtkinter.CTkLabel(master=window, image=img)
label_img.place(x=50, y=65)


# frame
frame = customtkinter.CTkFrame(master=window, width=350, height=396)
frame.pack(side=(RIGHT))


# frame widgets
label = customtkinter.CTkLabel(master=frame, text='Login', font=(
    'Roboto', 20, 'bold'), text_color=('white'))
label.place(x=25, y=5)

entry1 = customtkinter.CTkEntry(
    master=frame,
    placeholder_text='Nome de Usuário',
    width=300, font=("Arial", 10)).place(x=25, y=105)

label1 = customtkinter.CTkLabel(
    master=frame,
    text='*Esse campo exige caracter obrigatório.',
    text_color='green').place(x=25, y=135)

entry2 = customtkinter.CTkEntry(
    master=frame,
    placeholder_text='Senha',
    width=300, font=("Arial", 10)).place(x=25, y=175)

label2 = customtkinter.CTkLabel(
    master=frame,
    text='*Esse campo exige caracter obrigatório.',
    text_color='green').place(x=25, y=205)

checkbox = customtkinter.CTkCheckBox(
    master=frame, text='Lembrar-se de mim sempre').place(x=25, y=235)

button = customtkinter.CTkButton(
    master=frame, text='LOGIN', width=300).place(x=25, y=285)


window.mainloop()
