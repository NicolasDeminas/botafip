from tkinter import *
from Afip import comprobantesRecibidosFood, comprobantesEmitidosFood, comprobantesRecibidosAnser,comprobantesEmitidosAnser

root = Tk()

compRecibidosFood = Button(root, text="Comprobantes Recibidos Food", command=comprobantesRecibidosFood)
compEmitidosFood = Button(root, text="Comprobantes Emitidos Food", command=comprobantesEmitidosFood)
compRecibidosAnser = Button(root, text="Comprobantes Recibidos Anser", command=comprobantesRecibidosAnser)
compEmitidosAnser = Button(root, text="Comprobantes Emitidos Anser", command=comprobantesEmitidosAnser)
compRecibidosFood.pack()
compEmitidosFood.pack()
compRecibidosAnser.pack()
compEmitidosAnser.pack()

root.mainloop()
