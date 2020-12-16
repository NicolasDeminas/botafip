from selenium import webdriver
from time import sleep
import paths.paths as paths
from Secret import username_food, username_anser, password_food, password_anser
from ordenar_archivos import *


class Afip:
    def Inicio(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)
        self.driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")
    

    def login(self, username, password):
        self.driver.find_element_by_name(paths.ingresar_usuario).send_keys(username)
        self.driver.find_element_by_name(paths.ingresar_usuario_boton).click()
        self.driver.find_element_by_name(paths.ingresar_contraseña).send_keys(password)
        self.driver.find_element_by_name(paths.ingresar_contraseña_boton).click()

    def menu_mis_comprobantes(self, boton_mis_comprobantes):
        self.driver.find_element_by_xpath(boton_mis_comprobantes).click()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
    
    def comprobantes_recibidos(self):
        self.driver.find_element_by_xpath(paths.comprobantes_recibidos).click()

    def comprobantes_emitidos(self):
        self.driver.find_element_by_xpath(paths.comprobantes_emitidos).click()
    
    def seleccionar_comprobantes(self, fecha):
        self.driver.find_element_by_xpath(paths.definir_fecha).clear()
        self.driver.find_element_by_xpath(paths.definir_fecha).send_keys(fecha)
        self.driver.find_element_by_xpath(paths.boton_aceptar_fecha).click()
        self.driver.find_element_by_id(paths.boton_buscar_comprobantes).click()
        
    def descargar_csv(self):
        sleep(20)
        self.driver.find_element_by_xpath(paths.descargar_csv).click()

    def cerrar(self):
        sleep(2)
        self.driver.quit()
    
    def descargar_comprobantes_recibidos(self, username, password, boton_mis_comprobantes):
        self.Inicio()
        self.login(username, password)
        self.menu_mis_comprobantes(boton_mis_comprobantes)
        self.comprobantes_recibidos()
        self.seleccionar_comprobantes(paths.fecha)
        self.descargar_csv()
        self.cerrar()

    def descargar_comprobantes_emitidos(self, username, password, boton_mis_comprobantes):
        self.Inicio()
        self.login(username, password)
        self.menu_mis_comprobantes(boton_mis_comprobantes)
        self.comprobantes_emitidos()
        self.seleccionar_comprobantes(paths.fecha)
        self.descargar_csv()
        self.cerrar()

bot = Afip()
def comprobantesRecibidosFood():
    bot.descargar_comprobantes_recibidos(username_food, password_food, paths.boton_mis_comprobantes_food)
    ordenar_archivos(carpeta_downloads, mis_comprobantes_recibidos_food, carpeta_comprobantes_recibidos)

def comprobantesEmitidosFood():
    bot.descargar_comprobantes_emitidos(username_food, password_food, paths.boton_mis_comprobantes_food)
    ordenar_archivos(carpeta_downloads, mis_comprobantes_emitidos_food, carpeta_comprobantes_emitidos)

def comprobantesRecibidosAnser():
    bot.descargar_comprobantes_recibidos(username_anser, password_anser, paths.boton_mis_comprobantes_anser)
    ordenar_archivos(carpeta_downloads, comprobantes_recibidos_anser, carpeta_comprobantes_recibidos_anser)

def comprobantesEmitidosAnser():
    bot.descargar_comprobantes_emitidos(username_anser, password_anser, paths.boton_mis_comprobantes_anser)
    ordenar_archivos(carpeta_downloads, comprobantes_emitidos_anser, carpeta_comprobantes_emitidos_anser)

    