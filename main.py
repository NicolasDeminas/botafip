from tkinter import Tk, mainloop, COMMAND, Button
from Afip import comprobantesRecibidosFood, comprobantesEmitidosFood, comprobantesRecibidosAnser,comprobantesEmitidosAnser

root = Tk()
root.geometry("400x200")

compRecibidosFood = Button(root, text="Comprobantes Recibidos Food", command=comprobantesRecibidosFood)
compEmitidosFood = Button(root, text="Comprobantes Emitidos Food", command=comprobantesEmitidosFood)
compRecibidosAnser = Button(root, text="Comprobantes Recibidos Anser", command=comprobantesRecibidosAnser)
compEmitidosAnser = Button(root, text="Comprobantes Emitidos Anser", command=comprobantesEmitidosAnser)

compRecibidosFood.grid(row=0, column=0)
compEmitidosFood.grid(row=1, column=0)
compRecibidosAnser.grid(row=0, column=1)
compEmitidosAnser.grid(row=1, column=1)

root.mainloop()
