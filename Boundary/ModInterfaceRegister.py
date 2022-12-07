from tkinter import font, messagebox
from tkinter import *

from Entity.DAO import UserCRUD
from Control.ModRegister import Register


class TopLevelRegister(Toplevel):
    def __init__(self, master=None):
        super().__init__(master, width=500, height=350, padx=30, pady=5, bg="#222831")
        self.defaultFont = None
        self.objReg = Register(self)
        self.master = master
        self.widgets()
        self.setFrameFont()

    def setFrameFont(self):
        self.defaultFont = font.nametofont("TkDefaultFont", self.master)
        self.defaultFont.config(family="Cascadia Code PL",
                                size=8,
                                weight=font.BOLD)

    def requiredInput(self):
        return len(self.user.get()) != 0 and len(self.password.get()) != 0 and len(self.email.get()) != 0

    def fnRegister(self):
        if self.requiredInput():
            if self.objReg.register():
                messagebox.showinfo("Registro", message="Usuario registrado correctamente")
            else:
                messagebox.showinfo("Registro", message="El usuario ya existe")
            self.destroy()
        else:
            messagebox.showerror(title="Datos requeridos", message="Rellene todos los campos")

    def widgets(self):
        self.frame = LabelFrame(self, text="Registrar usuario", bg="#222831", fg="#00ADB5", pady=5, padx=10,
                           font=("Cascadia Code PL Semibold", 12, font.ITALIC))
        self.frame.grid(row=0, column=0, columnspan=3, pady=20)

        Label(self.frame, text='Usuario: ', bg="#222831", fg="#00ADB5", pady=5).grid(row=1, column=0)
        self.user = Entry(self.frame, bg="#393E46")
        self.user.grid(row=1, column=1)

        Label(self.frame, text='Email: ', bg="#222831", fg="#00ADB5", pady=5).grid(row=2, column=0)
        self.email = Entry(self.frame, bg="#393E46")
        self.email.grid(row=2, column=1)

        Label(self.frame, text='Contraseña: ', bg="#222831", fg="#00ADB5", pady=5).grid(row=3, column=0)
        self.password = Entry(self.frame, bg="#393E46", show="*")
        self.password.grid(row=3, column=1)

        self.btnRegister = Button(self.frame, text="Registrar", bg="#00ADB5", width=18,
                                  command=self.fnRegister)
        self.btnRegister.grid(row=4, column=0, sticky="s", columnspan=2, pady=10)