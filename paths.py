ingresar_usuario = "F1:username"
ingresar_usuario_boton = "F1:btnSiguiente"
ingresar_contraseña = "F1:password"
ingresar_contraseña_boton = "F1:btnIngresar"
boton_mis_comprobantes_food = "/html/body/main/section/div/div[43]/div/div/div/div[2]/h4"
boton_mis_comprobantes_anser = "/html/body/main/section[1]/div/div[31]/div/div/div/div[2]/h4"
comprobantes_recibidos = "/html/body/main/div/section/div/div/div[3]/a"
comprobantes_emitidos = "/html/body/main/div/section/div/div/div[2]/a"
definir_fecha = "/html/body/main/div/section/div/div/div[1]/div/div[1]/div/div/input"
boton_aceptar_fecha = "/html/body/div/div[3]/div/button[1]"
boton_buscar_comprobantes = "buscarComprobantes"
descargar_csv = "/html/body/main/div/section/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/button[1]"

from datetime import date, timedelta

hoy = date.today()
mesAnterior = hoy - timedelta(days=31)
hoy = hoy.strftime("%d/%m/%Y")
mesAnterior = mesAnterior.strftime("%d/%m/%Y")
fecha = mesAnterior," - ",hoy