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
comprobantes_recibidos_sanpina = 'Mis Comprobantes Recibidos - CUIT 30717641449'
comprobantes_emitidos_sanpina = 'Mis Comprobantes Emitidos - CUIT 30717641449'
carpeta_comprobantes_recibidos_sanpina = carpeta_downloads + '/Comprobantes recibidos Sanpina/'
carpeta_comprobantes_emitidos_sanpina = carpeta_downloads + '/Comprobantes emitidos Sanpina/'
archivos_acreditaciones = 'Acreditaciones_GO_30698322337'
carpeta_acreditaciones = carpeta_downloads + '/Archivos acreditaciones sueldos/'
pdfs = '.pdf'
txts = '.TXT'
csv = '.csv'
jpeg = '.jpeg'
carpeta_pdfs = carpeta_downloads + '/Pdfs/'
carpeta_txts = carpeta_downloads + '/Txts/'
carpeta_csv = carpeta_downloads + '/csv/'
carpeta_jpeg = carpeta_downloads + '/jpeg/'
carpeta_txt_sueldos_food = carpeta_downloads + 'TXTs Sueldos/Libro Sueldos Digital/'
carpeta_txt_sueldos_anser = carpeta_downloads + 'TXTs Sueldos Anser/Libro de sueldos digital/'
carpeta_txt_sueldos_sanpina = carpeta_downloads + 'TXTs Sueldos Sanpina/Libro de sueldos digital/'


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

def ordenarVarios(carpeta_a_ordenar, tipoArchivo, carpetaDestino):
    directorio = pathlib.Path(carpeta_a_ordenar)
    for archivo in directorio.iterdir():
        a = archivo.name.find(tipoArchivo)
        if a >= 0:
            fecha_creacion = time.ctime(os.path.getmtime(carpeta_a_ordenar +'/'+ archivo.name))
            fecha = datetime.datetime.strptime(fecha_creacion, "%a %b %d %H:%M:%S %Y")
            fecha = (datetime.datetime.strftime(fecha, '%Y-%m-%d-%H%M%S'))
            comprobante = str(fecha) + ' - ' + archivo.name
            shutil.move(carpeta_a_ordenar + archivo.name, carpetaDestino + comprobante )

def ordenarArchivosSueldos(carpeta_a_ordenar, periodo, carpetaDestino):
    directorio = pathlib.Path(carpeta_a_ordenar)
    for archivo in directorio.iterdir():
        a = archivo.name.find("Liquidacion_")
        if a >= 0:
            liquidacion = periodo + '-' + archivo.name
            shutil.move(carpeta_a_ordenar + archivo.name, carpetaDestino + liquidacion)
        
def agrupar(carpeta, periodo):
    directorio = pathlib.Path(carpeta)
    with open(carpeta + '/' + periodo + ' - Agrupado.xls', 'w') as f:
        for archivo in directorio.iterdir():
            a = archivo.name.find(periodo)
            if a == 0:
                with open(archivo, 'r') as archivo_sueldos:
                    for linea in archivo_sueldos:
                        #print(linea)
                        pos = linea.find('03')
                        #print(pos)
                        if pos == 0:
                            print(linea, file=f)



def ordenarTodo():
    ordenarVarios(carpeta_downloads, archivos_acreditaciones, carpeta_acreditaciones)
    ordenarVarios(carpeta_downloads, pdfs, carpeta_pdfs)
    ordenarVarios(carpeta_downloads, txts, carpeta_txts)
    ordenar_archivos(carpeta_downloads, mis_comprobantes_recibidos_food, carpeta_comprobantes_recibidos)
    ordenar_archivos(carpeta_downloads,mis_comprobantes_emitidos_food, carpeta_comprobantes_emitidos)
    ordenar_archivos(carpeta_downloads, comprobantes_recibidos_anser, carpeta_comprobantes_recibidos_anser)
    ordenar_archivos(carpeta_downloads, comprobantes_emitidos_anser, carpeta_comprobantes_emitidos_anser)
    ordenar_archivos(carpeta_downloads, comprobantes_recibidos_sanpina, carpeta_comprobantes_recibidos_sanpina)
    ordenar_archivos(carpeta_downloads, comprobantes_emitidos_sanpina, carpeta_comprobantes_emitidos_sanpina)
    ordenarVarios(carpeta_downloads, csv, carpeta_csv)
    ordenarVarios(carpeta_downloads, jpeg, carpeta_jpeg)


#ordenarTodo()