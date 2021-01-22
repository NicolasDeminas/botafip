path = "C:/Users/Nicolas/Google Drive/Python/BotAfip/chromedriver.exe"

ingresar_usuario = "F1:username"
ingresar_usuario_boton = "F1:btnSiguiente"
ingresar_contraseña = "F1:password"
ingresar_contraseña_boton = "F1:btnIngresar"
boton_mis_comprobantes_food = "/html/body/main/section/div/div[43]/div/div/div/div[2]/h4"
boton_mis_comprobantes_anser = "/html/body/main/section[2]/div/div[31]/div/div/div/div[2]/h4"
comprobantes_recibidos = "/html/body/main/div/section/div/div/div[3]/a"
comprobantes_emitidos = "/html/body/main/div/section/div/div/div[2]/a"
definir_fecha = "/html/body/main/div/section/div/div/div[1]/div/div[1]/div/div/input"
boton_aceptar_fecha = "/html/body/div/div[3]/div/button[1]"
boton_buscar_comprobantes = "buscarComprobantes"
descargar_csv = "/html/body/main/div/section/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/button[1]"
empresa = "/html/body/form/main/div/div/div[2]/div/div/div/a"


from datetime import date, timedelta

hoy = date.today()
mesAnterior = hoy - timedelta(days=31)
hoy = hoy.strftime("%d/%m/%Y")
mesAnterior = mesAnterior.strftime("%d/%m/%Y")
fecha = mesAnterior," - ",hoy

import datetime
import calendar
 
def fechas_mes():
    fecha_desde=input("Indique la fecha de inicio del mes: ")
    fecha_hasta=input("Indique la fecha de finalización del mes: ")
    return fecha_desde, fecha_hasta


