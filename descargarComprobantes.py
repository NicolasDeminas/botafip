import misComprobantes
import sys

placeholder, username, password, empresa, tipoComprobante, dias = sys.argv
dias = int(dias)
misComprobantes.misComprobantes = misComprobantes.misComprobantes()
misComprobantes.misComprobantes.descargarComprobantes(username, password, empresa, tipoComprobante, dias)