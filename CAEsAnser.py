import Afip
from Secret import username_anser, password_anser
import paths

bot_anser = Afip.Afip()
bot_anser.descargar_comprobantes_recibidos(username_anser, password_anser, paths.boton_mis_comprobantes_anser)
