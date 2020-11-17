import Afip
from Secret import username_food, password_food
import paths

bot_food = Afip.Afip()

tipo = input("Seleccione una opcion: Emitidos (E) o Recibidos (R)  ")
if tipo == "E" or tipo == "e":
    bot_food.descargar_comprobantes_emitidos(username_food, password_food, paths.boton_mis_comprobantes_food)
elif tipo == "R" or tipo == "r":
    bot_food.descargar_comprobantes_recibidos(username_food, password_food, paths.boton_mis_comprobantes_food)
    