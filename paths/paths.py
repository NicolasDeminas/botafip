path = "C:/Users/Nicolas/Google Drive/Python/BotAfip/chromedriver.exe"

ingresar_usuario = "F1:username"
ingresar_usuario_boton = "F1:btnSiguiente"
ingresar_contraseña = "F1:password"
ingresar_contraseña_boton = "F1:btnIngresar"
definir_fecha = "/html/body/main/div/section/div/div/div[1]/div/div[1]/div/div/input"
boton_aceptar_fecha = "/html/body/div/div[3]/div/button[1]"
boton_buscar_comprobantes = "buscarComprobantes"
descargar_csv = "/html/body/main/div/section/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/button[1]"
                
# descargar_csv = "/html/body/main/div/section/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/button[1]/span"


from datetime import date, timedelta
def fecha(dias):
    hoy = date.today()
    fechaInicio = hoy - timedelta(days=dias)
    hoy = hoy.strftime("%d/%m/%Y")
    fechaInicio = fechaInicio.strftime("%d/%m/%Y")
    return f'{fechaInicio} - {hoy}'


import datetime
import calendar
 
def fechas_mes():
    fecha_desde=input("Indique la fecha de inicio del mes: ")
    fecha_hasta=input("Indique la fecha de finalización del mes: ")
    return fecha_desde, fecha_hasta


