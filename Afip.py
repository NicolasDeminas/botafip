from selenium import webdriver
from time import sleep
import paths

path = "C:/Program Files (x86)/chromedriver.exe"

class Afip:
    def Inicio(self):
        self.driver = webdriver.Chrome(path)
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

    # def __init__(self, username, password, boton_mis_comprobantes):
    #     self.descargar_comprobantes_recibidos(username, password, boton_mis_comprobantes)



