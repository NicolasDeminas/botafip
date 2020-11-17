import Afip
from Secret import username_food, password_food, username_anser, password_anser
import paths

empresa = input("Para que empresa desea descargar CAEs? Ingrese F para Food Corner o A para Anser SRL: ")
if empresa == "F" or empresa == "f":
    bot_food = Afip.Afip(username_food, password_food, paths.boton_mis_comprobantes_food)
elif empresa == "A" or empresa == "a":
    bot_anser = Afip.Afip(username_anser, password_anser, paths.boton_mis_comprobantes_anser)
#elif empresa == "E" or empresa == "e":
    #Afip.Afip.descargar_comprobantes_emitidos(username_food, password_food, paths.boton_mis_comprobantes_food)
else:
    print("Empresa incorrecta, por favor vuelva a intentarlo")
