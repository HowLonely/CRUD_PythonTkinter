from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox
from Entity.DAO import ProductCRUD, UserCRUD
from Entity.DTO.Product import Product


class TopLevelModify(Toplevel):
    def __init__(self, objMain=None, master=None, old_name=None, old_price=None, old_categ=None, id_prod=None,
                 user=None):
        super().__init__(master, bg="#222831")
        self.objMain = objMain
        self.master = master
        self.user = user
        self.old_name = old_name
        self.old_price = old_price
        self.old_categ = old_categ
        self.id_prod = id_prod
        self.widgets()

    def edit_product(self):
        new_name = self.new_name.get()
        new_price = self.new_price.get()

        if len(self.new_name.get()) == 0:
            new_name = self.old_name
        if len(self.new_price.get()) == 0:
            new_price = self.old_price
        if len(self.new_categ.get()) == 0:
            new_id_categ = ProductCRUD.show_categ_by_name(self.old_categ)[0]
        else:
            new_id_categ = ProductCRUD.show_categ_by_name(self.new_categ.get())[0]

        date = datetime.today().date()
        id_user = UserCRUD.show_one(self.user)[0]
        prod = Product(self.id_prod, new_name, new_price, date, new_id_categ, id_user)
        ProductCRUD.modify(prod)
        self.objMain.fill_table()
        self.destroy()

    def fillBox(self):
        data = ProductCRUD.show_category()
        new_data = []
        for i in range(len(data)):
            new_data.append(str(data[i][1]).capitalize())
        return new_data

    def widgets(self):
        self.frame = LabelFrame(self, text="Modificar registro", padx=10, pady=10, bg="#222831", fg="#00ADB5")
        self.frame.grid(column=0)
        Label(self.frame, text="Nombre anterior: ", bg="#222831", fg="#00ADB5").grid(row=0, column=1)
        Entry(self.frame, textvariable=StringVar(self.frame, value=self.old_name), state='readonly').grid(row=0,
                                                                                                          column=2)

        Label(self.frame, text="Nuevo nombre: ", bg="#222831", fg="#00ADB5").grid(row=1, column=1)
        self.new_name = Entry(self.frame)
        self.new_name.grid(row=1, column=2)

        Label(self.frame, text="Precio anterior: ", bg="#222831", fg="#00ADB5").grid(row=2, column=1)
        field_oldPrice = Entry(self.frame, textvariable=StringVar(self.frame, value=self.old_price), state='readonly')
        field_oldPrice.grid(row=2, column=2)

        Label(self.frame, text="Nuevo Precio: ", bg="#222831", fg="#00ADB5").grid(row=3, column=1)
        self.new_price = Entry(self.frame)
        self.new_price.grid(row=3, column=2)

        Label(self.frame, text="Categoria anterior:", bg="#222831", fg="#00ADB5").grid(row=4, column=1)
        Entry(self.frame, textvariable=StringVar(self.frame, value=self.old_categ), state='readonly').grid(row=4,
                                                                                                           column=2)

        Label(self.frame, text="Nueva categoria:", bg="#222831", fg="#00ADB5").grid(row=5, column=1)
        self.new_categ = self.boxCategory = Combobox(self.frame, width=18, state='readonly',
                                                     values=self.fillBox())
        self.new_categ.grid(row=5, column=2)

        Button(self.frame, text="Actualizar", bg="#00ADB5",
               command=self.edit_product).grid(row=6, column=1, pady=10, columnspan=2)
