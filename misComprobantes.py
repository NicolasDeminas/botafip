from selenium import webdriver
from time import sleep
from Afip import Afip
import paths.paths as paths


class misComprobantes:
    def Iniciar(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)
        
    def empresa(self, empresa):
        for n in range(1, 10):
            try:
                representar = self.driver.find_element_by_xpath("/html/body/form/main/div/div/div[2]/div/div[" + str(n) + "]/div/a")
                r = representar.text
                if r.find(empresa) >= 0:
                    representar.click()
                    break
            except Exception:
                break

    def comprobantes(self, tipoComprobante):
        sleep(1)
        for c in range(2, 5):
            comp = self.driver.find_element_by_xpath("/html/body/main/div/section/div/div/div[" + str(c) + "]/a")
            compr = comp.text
            if compr.find(tipoComprobante) >= 0:
                comp.click()
                break
    
    def seleccionarComprobantes(self):
        self.driver.find_element_by_xpath(paths.definir_fecha).clear()
        self.driver.find_element_by_xpath(paths.definir_fecha).send_keys(paths.fecha)
        self.driver.find_element_by_xpath(paths.boton_aceptar_fecha).click()
        self.driver.find_element_by_id(paths.boton_buscar_comprobantes).click()
        
    def descargarCSV(self):
        sleep(20)
        self.driver.find_element_by_xpath(paths.descargar_csv).click()

    def descargarComprobantes(self, username, password, empresa, tipoComprobante):
        Afip.Inicio(self)
        Afip.login(self, username, password)
        Afip.buscarMenu(self, "Mis Comprobantes")
        self.empresa(empresa)
        self.comprobantes(tipoComprobante)
        self.seleccionarComprobantes()
        self.descargarCSV()
        Afip.cerrar(self)
        
