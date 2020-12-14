import os,datetime, time, pathlib
import shutil

carpeta_a_ordenar = 'c:/Users/Nicolas/Downloads/'
mis_comprobantes_recibidos_base='Mis Comprobantes Recibidos - CUIT 30698322337'
carpeta_comprobantes_recibidos = carpeta_a_ordenar + '/Comprobantes recibidos/'
mis_comprobantes_emitidos_base='Mis Comprobantes Emitidos - CUIT 30698322337'
carpeta_comprobantes_emitidos = carpeta_a_ordenar + '/Comprobantes emitidos/'
comprobantes_recibidos_anser = 'Mis Comprobantes Recibidos - CUIT 30689189233'
comprobantes_emitidos_anser = 'Mis Comprobantes Emitidos - CUIT 30689189233'
carpeta_comprobantes_recibidos_anser = carpeta_a_ordenar + '/Comprobantes recibidos Anser/'
carpeta_comprobantes_emitidos_anser = carpeta_a_ordenar + '/Comprobantes emitidos Anser/'




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

ordenar_archivos(carpeta_a_ordenar, mis_comprobantes_recibidos_base, carpeta_comprobantes_recibidos)
ordenar_archivos(carpeta_a_ordenar,mis_comprobantes_emitidos_base, carpeta_comprobantes_emitidos)
ordenar_archivos(carpeta_a_ordenar, comprobantes_recibidos_anser, carpeta_comprobantes_recibidos_anser)
ordenar_archivos(carpeta_a_ordenar, comprobantes_emitidos_anser, carpeta_comprobantes_emitidos_anser)
