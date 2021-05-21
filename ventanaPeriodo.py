from tkinter import *
from tkinter import ttk
import libroSueldosDigital
import Secret
from ordenar_archivos import ordenarArchivosSueldos, carpeta_txt_sueldos_food, carpeta_downloads, agrupar, carpeta_txt_sueldos_anser

libroSueldosDigital.LibroSueldos = libroSueldosDigital.LibroSueldos()

def ventanaPeriodoFood():
    meses = ['01', '02', '03', '04', '05', '06','07','08','09','10','11','12',]
    años = ['2019', '2020', '2021', '2022', '2023', '2024','2025','2026','2027','2028','2029','2030',]

    def libroSueldosFood():
        periodo = mes.get() + "/" + año.get()
        periodo_ordenar = año.get() + mes.get()
        libroSueldosDigital.LibroSueldos.libroSueldosDigital(Secret.usernameFood, Secret.passwordFood, periodo, "30-69832233-7 FOOD CORNER S A")
        ordenarArchivosSueldos(carpeta_downloads, periodo_ordenar, carpeta_txt_sueldos_food)
        agrupar(carpeta_txt_sueldos_food, periodo_ordenar)


    ventana = Tk()
    ventana.title("lista desplegable")
    ventana.geometry("500x100")

    mes = ttk.Combobox(ventana, width=20, state="readonly")
    mes.place(x=25, y=30)
    mes['values'] = meses

    año = ttk.Combobox(ventana, width=20, state="readonly")
    año.place(x=230, y=30)
    año['values'] = años

    Button(ventana, text="Periodo", command=libroSueldosFood).place(x=400, y=25)

    ventana.mainloop()



def ventanaPeriodoAnser():
    meses = ['01', '02', '03', '04', '05', '06','07','08','09','10','11','12',]
    años = ['2019', '2020', '2021', '2022', '2023', '2024','2025','2026','2027','2028','2029','2030',]

    def libroSueldosAnser():
        periodo = mes.get() + "/" + año.get()
        periodo_ordenar = año.get() + mes.get()
        libroSueldosDigital.LibroSueldos.libroSueldosDigital(Secret.usernameAnser, Secret.passwordAnser, periodo, "ANSER")
        ordenarArchivosSueldos(carpeta_downloads, periodo_ordenar, carpeta_txt_sueldos_anser)
        agrupar(carpeta_txt_sueldos_anser, periodo_ordenar)

    ventana = Tk()
    ventana.title("lista desplegable")
    ventana.geometry("500x100")

    mes = ttk.Combobox(ventana, width=20, state="readonly")
    mes.place(x=25, y=30)
    mes['values'] = meses

    año = ttk.Combobox(ventana, width=20, state="readonly")
    año.place(x=230, y=30)
    año['values'] = años

    Button(ventana, text="Periodo", command=libroSueldosAnser).place(x=400, y=25)

    ventana.mainloop()
