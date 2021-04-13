from selenium import webdriver
from time import sleep
from Afip import Afip
import paths.paths as paths
import Secret

class Coprib:
    def Iniciar(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)

    def empresa(self, cuit):
        for e in range(1, 10):   
            empresa = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/form/div[2]/div/select/option[" + str(e) + "]")
            empr = empresa.text
            if empr.find(cuit) >= 0:
                empresa.click()
                self.driver.find_element_by_id("btnContinuarADatosContribuyente").click()
                break

    def tipoConsulta(self):
        self.driver.find_element_by_name("btnConsultaPorFecha").click()
        
    def definirPeriodo(self):
        self.driver.find_element_by_id("fechaDesde").clear()
        self.driver.find_element_by_id("fechaDesde").send_keys("01/03/2021")
        self.driver.find_element_by_id("fechaHasta").clear()
        self.driver.find_element_by_id("fechaHasta").send_keys("31/03/2021")
        self.driver.find_element_by_name("btnBuscarConsultaPorPeriodo").click()
        
        #self.driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/form/div[4]/div[2]/table/tbody/tr[1]/td[3]/input").click()

    def detallePeriodo(self):
        self.driver.find_element_by_name("btnDetalleSiprib").click()
        sleep(10)

    def exportarExcel(self):
        self.driver.find_element_by_id("btnExportarDatos").click()

    def descargarCoprib(self, username, password, cuit):
        Afip.Inicio(self)
        Afip.login(self, username, password)
        Afip.buscarMenu(self, "API-Santa Fe- COPRIB")
        self.empresa(cuit)
        self.tipoConsulta()
        #self.definirPeriodo()
        self.detallePeriodo()
        self.exportarExcel()
        Afip.cerrar(self)        

