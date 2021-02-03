from tkinter import Tk, mainloop, COMMAND, Button
#from Afip import comprobantesEmitidosFood, comprobantesRecibidosAnser,comprobantesEmitidosAnser
import misComprobantes
import Secret
import ordenar_archivos

misComprobantes.misComprobantes = misComprobantes.misComprobantes()
def comprobantesRecibidosFood():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameFood, Secret.passwordFood, "FOOD CORNER", "Recibidos")
    ordenar_archivos.ordenarTodo
def comprobantesEmitidosFood():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameFood, Secret.passwordFood, "FOOD CORNER", "Emitidos")
    ordenar_archivos.ordenarTodo
def comprobantesRecibidosAnser():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameAnser, Secret.passwordAnser, "ANSER", "Recibidos")
    ordenar_archivos.ordenarTodo
def comprobantesEmitidosAnser():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameAnser, Secret.passwordAnser, "ANSER", "Emitidos")
    ordenar_archivos.ordenarTodo

root = Tk()
root.geometry("450x200")

compRecibidosFood = Button(root, text="Comprobantes Recibidos Food", command=comprobantesRecibidosFood)
compEmitidosFood = Button(root, text="Comprobantes Emitidos Food", command=comprobantesEmitidosFood)
compRecibidosAnser = Button(root, text="Comprobantes Recibidos Anser", command=comprobantesRecibidosAnser)
compEmitidosAnser = Button(root, text="Comprobantes Emitidos Anser", command=comprobantesEmitidosAnser)
ordenarTodo = Button(root, text="Ordenar archivos", command=ordenar_archivos.ordenarTodo)

compRecibidosFood.grid(row=0, column=0)
compEmitidosFood.grid(row=1, column=0)
compRecibidosAnser.grid(row=0, column=2)
compEmitidosAnser.grid(row=1, column=2)
ordenarTodo.grid(row=3, column=1)

root.mainloop()
