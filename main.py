from tkinter import Tk, mainloop, COMMAND, Button
from tkinter.constants import SE
import misComprobantes
import Secret
import ordenar_archivos
import coprib
from ventanaPeriodo import ventanaPeriodoFood, ventanaPeriodoAnser, ventanaPeriodoSanpina


misComprobantes.misComprobantes = misComprobantes.misComprobantes()
coprib.Coprib = coprib.Coprib()
# libroSueldosDigital.LibroSueldos = libroSueldosDigital.LibroSueldos()

def comprobantesRecibidosFood():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameFood, Secret.passwordFood, "FOOD CORNER", "Recibidos", 31)
    ordenar_archivos.ordenarTodo()
def comprobantesEmitidosFood():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameFood, Secret.passwordFood, "FOOD CORNER", "Emitidos", 10)
    ordenar_archivos.ordenarTodo
def comprobantesRecibidosSanpina():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameSanpina, Secret.passwordSanpina, "SANPINA", "Recibidos", 31)
    ordenar_archivos.ordenarTodo()
def comprobantesEmitidosSanpina():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameSanpina, Secret.passwordSanpina, "SANPINA", "Emitidos", 10)
    ordenar_archivos.ordenarTodo
def comprobantesRecibidosAnser():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameAnser, Secret.passwordAnser, "ANSER", "Recibidos", 31)
    ordenar_archivos.ordenarTodo
def comprobantesEmitidosAnser():
    misComprobantes.misComprobantes.descargarComprobantes(Secret.usernameAnser, Secret.passwordAnser, "ANSER", "Emitidos", 10)
    ordenar_archivos.ordenarTodo
def copribFood():
    coprib.Coprib.descargarCoprib(Secret.usernameFood, Secret.passwordFood, Secret.cuitFood)
def copribAnser():
    coprib.Coprib.descargarCoprib(Secret.usernameAnser, Secret.passwordAnser, Secret.cuitAnser)
# def ventanaPeriodoFood():
#     ventanaPeriodoFood
# def ventanaPeriodoAnser():
#     ventanaPeriodoAnser
# def libroSueldosFood():
#     libroSueldosDigital.LibroSueldos.libroSueldosDigital(Secret.usernameFood, Secret.passwordFood, "04/2021")

root = Tk()
root.geometry("650x200")

compRecibidosFood = Button(root, text="Comprobantes Recibidos Food", command=comprobantesRecibidosFood)
compEmitidosFood = Button(root, text="Comprobantes Emitidos Food", command=comprobantesEmitidosFood)
compRecibidosSanpina = Button(root, text="Comprobantes Recibidos Sanpina", command=comprobantesRecibidosSanpina)
compEmitidosSanpina = Button(root, text="Comprobantes Emitidos Sanpina", command=comprobantesEmitidosSanpina)
compRecibidosAnser = Button(root, text="Comprobantes Recibidos Anser", command=comprobantesRecibidosAnser)
compEmitidosAnser = Button(root, text="Comprobantes Emitidos Anser", command=comprobantesEmitidosAnser)
ordenarTodo = Button(root, text="Ordenar archivos", command=ordenar_archivos.ordenarTodo)
copribFood = Button(root, text="Descargar Coprib Food", command=copribFood)
copribAnser = Button(root, text="Descargar Coprib Anser", command=copribAnser)
libroSueldosFood = Button(root, text="Libro Sueldos Food", command=ventanaPeriodoFood)
libroSueldosSanpina = Button(root, text="Libro Sueldos Sanpina", command=ventanaPeriodoSanpina)
libroSueldosAnser = Button(root, text="Libro Sueldos Anser", command=ventanaPeriodoAnser)
#libroSueldosFood = Button(root, text="Libro Sueldos Digital Food", command=libroSueldosFood)

compRecibidosFood.grid(row=0, column=0)
compEmitidosFood.grid(row=1, column=0)
copribFood.grid(row=2, column=0)
compRecibidosAnser.grid(row=0, column=2)
compEmitidosAnser.grid(row=1, column=2)
copribAnser.grid(row=2, column=2)
libroSueldosFood.grid(row=3, column=0)
libroSueldosAnser.grid(row=3, column=2)
compRecibidosSanpina.grid(row=0, column=1)
compEmitidosSanpina.grid(row=1, column=1)
libroSueldosSanpina.grid(row=3, column=1)
ordenarTodo.grid(row=6, column=1)

root.mainloop()
