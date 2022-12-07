from tkinter import *
from tkinter import font
from Boundary.ModInterfaceRegister import TopLevelRegister
from Boundary.ModInterfaceMain import FrameMain
from Control.ModLogin import Login
from tkinter import messagebox


class FrameLogin(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=500, height=350, padx=30, pady=10, bg="#222831")
        self.defaultFont = None
        self.objLogin = Login(self)
        self.master = master
        self.pack()
        self.widgets()
        self.setFrameFont()

    def setFrameFont(self):

        self.defaultFont = font.nametofont("TkDefaultFont", self.master)
        self.defaultFont.config(family="Cascadia Mono PL",
                                size=8,
                                weight=font.BOLD)

    def fnRegister(self, event):
        TopLevelRegister(self.master)

    def fnLogin(self):
        #Abre el menu principal
        if self.objLogin.verifLogIn():
            self.user = self.field_user.get()
            self.master.destroy()
            main = Tk()
            main.title("Sistema - Principal")
            main.eval('tk::PlaceWindow . center')
            main.resizable(False, False)
            user = self.user
            app = FrameMain(main, user)
            app.mainloop()
        else:
            messagebox.showerror(message='Nombre de usuario o contraseña incorrectas', title="Error inicio sesión")

    def widgets(self):
        self.frame = LabelFrame(self, text="Login sistema", bg="#222831", fg="#00ADB5",  pady=5, padx=10,
                               font=("Cascadia Mono PL", 12, font.BOLD))
        self.frame.grid(row=0, columnspan=2, pady=5)

        self.lbl_user = Label(self.frame, text="Usuario:", bg="#222831", fg="#00ADB5")
        self.lbl_user.grid(row=2, sticky="w")

        self.field_user = Entry(self.frame, width=33, bg="#393E46",
                                font=("Cascadia Mono PL Semibold", 9, font.ITALIC))
        self.field_user.grid(row=3)

        self.lbl_pass = Label(self.frame, text="Contraseña", bg="#222831", fg="#00ADB5")
        self.lbl_pass.grid(row=4, sticky="w")

        self.field_pass = Entry(self.frame, width=33, show="*", bg="#393E46",
                                font=("Cascadia Mono PL Semibold", 9, font.ITALIC))
        self.field_pass.grid(row=5, columnspan=2, sticky="w")

        self.lbl_empty = Label(self.frame, text="No tienes una cuenta?", bg="#222831", fg="#00ADB5", pady=10)
        self.lbl_empty.grid(row=6, sticky="w")

        self.lbl_register = Label(self.frame, text="registrate aquí", bg="#222831", fg="blue", cursor="hand2",
                                  font=("Cascadia Mono PL Italic", 8, 'underline'))
        self.lbl_register.grid(row=6, sticky="e", columnspan=2)
        self.lbl_register.bind("<Button>", self.fnRegister)

        self.btn_login = Button(self.frame, text="Iniciar sesión", bg="#00ADB5", width=20,
                                command=self.fnLogin)
        self.btn_login.grid(row=7)
