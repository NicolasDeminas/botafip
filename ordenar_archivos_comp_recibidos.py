import os,datetime, time, pathlib
import shutil

carpeta_a_ordenar = 'c:/Users/Nicolas/Downloads/'
mis_comprobantes_base='Mis Comprobantes Recibidos - CUIT 30698322337'
carpeta_destino = carpeta_a_ordenar + '/Comprobantes recibidos/'

def ordenar_archivos(carpeta_a_ordenar, mis_comprobantes_base, carpeta_destino):
    directorio = pathlib.Path(carpeta_a_ordenar)
    for archivo in directorio.iterdir():
        a = archivo.name.find(mis_comprobantes_base)
        if a >= 0:
            fecha_creacion = time.ctime(os.path.getmtime(carpeta_a_ordenar +'/'+ archivo.name))
            fecha = datetime.datetime.strptime(fecha_creacion, "%a %b %d %H:%M:%S %Y")
            fecha = (datetime.datetime.strftime(fecha, '%Y-%m-%d-%H%M%S'))
            comprobante = mis_comprobantes_base + ' - ' + str(fecha) + '.csv'
            shutil.move(carpeta_a_ordenar + archivo.name, carpeta_destino + comprobante)

ordenar_archivos(carpeta_a_ordenar, mis_comprobantes_base, carpeta_destino)
