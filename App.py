from tkinter import Tk
from Boundary.ModInterfaceLogin import FrameLogin

root = Tk()
root.title("Sistema - Login")

root.eval('tk::PlaceWindow . center')
root.resizable(False, False)

app = FrameLogin(root)
app.mainloop()
