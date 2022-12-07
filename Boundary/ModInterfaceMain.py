from tkinter import font, messagebox
from tkinter import *
from tkinter.ttk import Treeview, Style, Combobox
from Control.ModMain import Main
from Entity.DAO import ProductCRUD


class FrameMain(Frame):
    def __init__(self, master=None, user=None):
        super().__init__(master, width=500, height=350, padx=30, pady=10, bg="#222831")
        self.user = user
        self.objMain = Main(self)
        self.tree = None
        self.defaultFont = None
        self.master = master
        self.pack()
        self.widgets()
        self.setFrameFont()

    def setFrameFont(self):
        self.defaultFont = font.nametofont("TkDefaultFont", self.master)
        self.defaultFont.config(family="Cascadia Mono PL",
                                size=9,
                                weight=font.BOLD)

    def applyTreeStyle(self):
        style = Style()
        style.theme_use('default')
        style.configure('Treeview',
                        background='#222831',
                        fieldbackground="#222831",
                        foreground='#00ADB5',
                        font=("Cascadia Mono PL", 8)
                        )
        style.configure('Treeview.Heading',
                        background='#222831',
                        fieldbackground="#222831",
                        foreground='#00ADB5',
                        font=("Cascadia Mono PL", 8)
                        )
        style.configure('Combobox',
                        backgroud='black')

    def validation(self):
        return len(self.nameProd.get()) != 0 and len(self.priceProd.get()) != 0 and len(self.boxCategory.get()) != 0

    def selectedFilter(self, event):
        if self.filterBox.get() == 'Mostrar todo':
            self.objMain.fill_table()
        else:
            self.objMain.fill_table_many(int(self.filterBox.get().split()[1]))


    def widgets(self):
        self.title = Label(self, text="Bienvenido {}".format(self.user), bg="#222831", fg="#00ADB5", pady=5,
                           font=("Cascadia Mono PL", 12, font.BOLD))
        self.title.grid(row=0, column=0, columnspan=3, sticky="w")

        self.frame = LabelFrame(self, text="Registrar un producto", padx=30, pady=5, bg="#222831", fg="#00ADB5")
        self.frame.grid(row=1, column=0, columnspan=3)

        Label(self.frame, text='Nombre: ', bg="#222831", fg="#00ADB5").grid(row=1, column=0, sticky="w")
        self.nameProd = Entry(self.frame)
        self.nameProd.grid(row=1, column=1, sticky="e")

        Label(self.frame, text='Precio: ', bg="#222831", fg="#00ADB5").grid(row=2, column=0, sticky="w")
        self.priceProd = Entry(self.frame)
        self.priceProd.grid(row=2, column=1, sticky="e")

        Label(self.frame, text='Categoria: ', bg="#222831", fg="#00ADB5").grid(row=3, column=0, sticky="w")
        self.boxCategory = Combobox(self.frame, width=18, state='readonly',
                                    values=self.objMain.boxCategoryFill())

        self.boxCategory.grid(row=3, column=1, sticky="w")

        Button(self.frame, text="Añadir", width=10, bg="#00ADB5",
               command=self.objMain.addProd) \
            .grid(row=4, columnspan=3, column=0, sticky="e", pady=5, padx=25)

        self.frTable = LabelFrame(self, text="Tabla de productos", pady=10, padx=10, bg="#222831", fg="#00ADB5")
        self.frTable.grid(row=2, column=0, columnspan=3)

        self.applyTreeStyle()

        self.tree = Treeview(self.frTable, height=10,
                             columns=['#1', '#2', '#3', '#4', '#5', '#6'],
                             show='headings')

        self.tree.grid(row=2, columnspan=2)
        self.tree.heading('#1', text='ID', anchor=CENTER)
        self.tree.heading('#2', text='Nombre', anchor=CENTER)
        self.tree.heading('#3', text='Precio', anchor=CENTER)
        self.tree.heading('#4', text='Categoría', anchor=CENTER)
        self.tree.heading('#5', text='Fecha', anchor=CENTER)
        self.tree.heading('#6', text='Dueño', anchor=CENTER)

        self.tree.column('#1', stretch=NO, width=30)
        self.tree.column('#2', stretch=NO, width=80)
        self.tree.column('#3', stretch=NO, width=60)
        self.tree.column('#4', stretch=NO, width=100)
        self.tree.column('#5', stretch=NO, width=80)
        self.tree.column('#6', stretch=NO, width=90)

        self.objMain.fill_table()

        Label(self.frTable, text='Filtrar: ', bg="#222831", fg="#00ADB5").grid(row=3, column=0, sticky="w")
        self.filterBox = Combobox(self.frTable, width=18, state='readonly',
                                    values=[ "Mostrar todo", "Mostrar 1", "Mostrar 2", "Mostrar 5"])
        self.filterBox.grid(row=3, column=0, sticky="ew", padx=80, pady=10, columnspan=1)
        self.filterBox.bind('<<ComboboxSelected>>', self.selectedFilter)


        self.btnEdit = Button(self.frTable, text='Modificar', width=15, bg="#00ADB5",
                              command=self.objMain.edit_prod)
        self.btnEdit.grid(row=4, column=0, sticky="w", padx=20)

        self.btnEliminar = Button(self.frTable, text='Eliminar', width=15, bg="#00ADB5",
                                  command=self.objMain.delete_prod)
        self.btnEliminar.grid(row=4, column=1, pady=5)
