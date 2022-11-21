
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()

window.title('Login Page')
window.geometry('400x500')
window.config(background = 'black')

user = input('enter id here: ')
pass_word = input('enter password here: ')


label1 = Label(text = 'Welcome to the login page!',background='light blue',foreground='black',font=('times new roman',20))
label1.place(x=60,y=15)


photo = Image.open(r"C:\Users\gul\PycharmProjects\pythonProject4\venv\company.png")
resize_photo = photo.resize((190,170))

img = ImageTk.PhotoImage(resize_photo)
ph = Label(window,image=img,background='black',height = 100,width = 100)
ph.place(x=155,y=75)

label1 = Label(text = 'Enter user_id/email here: ',background='black',foreground='white',font=('times new roman',15))
label1.place(x=50,y=200)

user_id = Entry(width=50)
user_id.place(x=50,y=250)

label2 = Label(text = 'Enter password here: ',background='black',foreground='white',font=('times new roman',15))
label2.place(x=50,y=300)

password = Entry(width=50)
password.place(x=50,y=350)

def login():
    a = user_id.get()
    if a == "":
        label3 = Label(window, text="please enter user id.",background='black', foreground='red', font=('times new roman', 11))
        label3.place(x=50, y=225)

    b = password.get()
    if b == "":
        label4 = Label(window, text="please enter password.",background='black', foreground='red', font=('times new roman', 11))
        label4.place(x=50, y=325)

    if a == user and b == pass_word:
        box = messagebox.showinfo("login", "Congrats! Login successful.")

    else:
        box1 = messagebox.showinfo("login", "Sorry, login failed. Please try again.")

button = Button(text = 'Login Here',command = login, background='yellow',font = ('Times new roman',13))
button.place(x=155,y=430)

window.mainloop()
