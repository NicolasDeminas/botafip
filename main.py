from tkinter import Tk, mainloop, COMMAND, Button
import misComprobantes
import Secret
import ordenar_archivos
import coprib

misComprobantes.misComprobantes = misComprobantes.misComprobantes()
coprib.Coprib = coprib.Coprib()
def comprobantesRecibidosFood():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameFood, Secret.passwordFood, "FOOD CORNER", "Recibidos")
    ordenar_archivos.ordenarTodo()
def comprobantesEmitidosFood():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameFood, Secret.passwordFood, "FOOD CORNER", "Emitidos")
    ordenar_archivos.ordenarTodo
def comprobantesRecibidosAnser():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameAnser, Secret.passwordAnser, "ANSER", "Recibidos")
    ordenar_archivos.ordenarTodo
def comprobantesEmitidosAnser():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameAnser, Secret.passwordAnser, "ANSER", "Emitidos")
    ordenar_archivos.ordenarTodo
def copribFood():
    coprib.Coprib.descargarCoprib(Secret.usernameFood, Secret.passwordFood, Secret.cuitFood)
def copribAnser():
    coprib.Coprib.descargarCoprib(Secret.usernameAnser, Secret.passwordAnser, Secret.cuitAnser)

root = Tk()
root.geometry("450x200")

compRecibidosFood = Button(root, text="Comprobantes Recibidos Food", command=comprobantesRecibidosFood)
compEmitidosFood = Button(root, text="Comprobantes Emitidos Food", command=comprobantesEmitidosFood)
compRecibidosAnser = Button(root, text="Comprobantes Recibidos Anser", command=comprobantesRecibidosAnser)
compEmitidosAnser = Button(root, text="Comprobantes Emitidos Anser", command=comprobantesEmitidosAnser)
ordenarTodo = Button(root, text="Ordenar archivos", command=ordenar_archivos.ordenarTodo)
copribFood = Button(root, text="Descargar Coprib Food", command=copribFood)
copribAnser = Button(root, text="Descargar Coprib Anser", command=copribAnser)


compRecibidosFood.grid(row=0, column=0)
compEmitidosFood.grid(row=1, column=0)
copribFood.grid(row=2, column=0)
compRecibidosAnser.grid(row=0, column=2)
compEmitidosAnser.grid(row=1, column=2)
copribAnser.grid(row=2, column=2)
ordenarTodo.grid(row=3, column=1)

root.mainloop()
