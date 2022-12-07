from tkinter import *
from tkinter import messagebox, ttk

from Entity.DAO import ProductCRUD
from Entity.DTO.Product import Product
from Entity.DAO import UserCRUD
from datetime import date
from Boundary.ModInterfaceModify import TopLevelModify
from Control import Others


class Main:
    def __init__(self, frame):
        self.db_rows = None
        self.data = []
        self.frame = frame

    def fill_table(self):
        # Cleaning table
        records = self.frame.tree.get_children()
        for element in records:
            self.frame.tree.delete(element)
        # query
        self.db_rows = ProductCRUD.show_all()
        for row in self.db_rows:
            self.frame.tree.insert('', 'end', text=row[1],
                                   values=(row[0], row[1], row[2], ProductCRUD.show_one_categ(row[4])[1],
                                           row[3], UserCRUD.search_index(row[5])[1]))

    def fill_table_many(self, quantity):
        # Cleaning table
        records = self.frame.tree.get_children()
        for element in records:
            self.frame.tree.delete(element)
        # query
        self.db_rows = ProductCRUD.show_many(quantity)
        for row in self.db_rows:
            self.frame.tree.insert('', 'end', text=row[1],
                                   values=(row[0], row[1], row[2], ProductCRUD.show_one_categ(row[4])[1],
                                           row[3], UserCRUD.search_index(row[5])[1]))

    def addProd(self):
        if Others.isNumeric(self.frame.priceProd.get()):
            if self.frame.validation():
                name = self.frame.nameProd.get()
                price = self.frame.priceProd.get()
                today = date.today()
                id_category = ProductCRUD.show_categ_by_name(self.frame.boxCategory.get())[0]
                id_user = UserCRUD.show_one(self.frame.user)[0]

                prod = Product("", name, price, today, id_category, id_user)
                ProductCRUD.insert(prod)

                #clear inputs
                self.frame.nameProd.delete(0, 'end')
                self.frame.priceProd.delete(0, 'end')
                self.frame.boxCategory.set('')

                self.fill_table()
            else:
                messagebox.showerror(title="Campos insuficientes", message="Nombre, precio y categoría necesarios")
        else:
            messagebox.showerror(title="Numero ingresado", message="El precio debe ser un número")


    def delete_prod(self):
        try:
            id_prod_selected = self.frame.tree.item(self.frame.tree.selection())['values'][0]
            ProductCRUD.delete(id_prod_selected)
            self.fill_table()
        except IndexError as e:
            messagebox.showerror(title="Error de seleccion", message="Seleccione un registro")

    def edit_prod(self):
        try:
            id_prod_selected = self.frame.tree.item(self.frame.tree.selection())['values'][0]

            old_name = self.frame.tree.item(self.frame.tree.selection())['values'][1]
            old_price = self.frame.tree.item(self.frame.tree.selection())['values'][2]
            old_category = self.frame.tree.item(self.frame.tree.selection())['values'][3]

            user = self.frame.user
            TopLevelModify(self, self.frame, old_name, old_price, old_category, id_prod_selected, user)


        except IndexError as e:
            messagebox.showerror(title="Error de seleccion", message="Seleccione un registro")

    def boxCategoryFill(self):
        data = ProductCRUD.show_category()
        new_data = []
        for i in range(len(data)):
            new_data.append(str(data[i][1]).capitalize())
        return new_data
