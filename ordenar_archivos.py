import os,datetime, time, pathlib
import shutil

carpeta_downloads = 'c:/Users/Nicolas/Downloads/'
mis_comprobantes_recibidos_food='Mis Comprobantes Recibidos - CUIT 30698322337'
carpeta_comprobantes_recibidos = carpeta_downloads + '/Comprobantes recibidos/'
mis_comprobantes_emitidos_food='Mis Comprobantes Emitidos - CUIT 30698322337'
carpeta_comprobantes_emitidos = carpeta_downloads + '/Comprobantes emitidos/'
comprobantes_recibidos_anser = 'Mis Comprobantes Recibidos - CUIT 30689189233'
comprobantes_emitidos_anser = 'Mis Comprobantes Emitidos - CUIT 30689189233'
carpeta_comprobantes_recibidos_anser = carpeta_downloads + '/Comprobantes recibidos Anser/'
carpeta_comprobantes_emitidos_anser = carpeta_downloads + '/Comprobantes emitidos Anser/'
archivos_acreditaciones = 'Acreditaciones_GO_30698322337'
carpeta_acreditaciones = 'Archivos acreditaciones sueldos'
pdfs = '.pdf'
carpeta_pdfs = 'Pdfs'



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

ordenar_archivos(carpeta_downloads, mis_comprobantes_recibidos_food, carpeta_comprobantes_recibidos)
ordenar_archivos(carpeta_downloads,mis_comprobantes_emitidos_food, carpeta_comprobantes_emitidos)
ordenar_archivos(carpeta_downloads, comprobantes_recibidos_anser, carpeta_comprobantes_recibidos_anser)
ordenar_archivos(carpeta_downloads, comprobantes_emitidos_anser, carpeta_comprobantes_emitidos_anser)


def ordenarVarios(carpeta_a_ordenar, tipoArchivo, carpetaDestino):
    directorio = pathlib.Path(carpeta_a_ordenar)
    for archivo in directorio.iterdir():
        a = archivo.name.find(tipoArchivo)
        if a >= 0:
            shutil.move(carpeta_a_ordenar + archivo.name, carpeta_a_ordenar + carpetaDestino )
        
ordenarVarios(carpeta_downloads, archivos_acreditaciones, carpeta_acreditaciones)
ordenarVarios(carpeta_downloads, pdfs, carpeta_pdfs)
