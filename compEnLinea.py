from selenium import webdriver
from time import sleep
from Afip import Afip
import paths.paths as paths

class CompEnLinea:
    def Iniciar(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)

    def empresa(self, empresa):
        for e in range(1, 10):
            empr = self.driver.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[4]/td/input["+ str(e) +"]")
            emp = empr.get_attribute("value")
            if emp.find(empresa) >= 0:
                empr.click()
                break

    def generarComprobantes(self, puntoDeVenta, tipoComprobante):
        self.driver.find_element_by_id("btn_gen_cmp").click()
        for puntoVenta in range(1,5):
            punto = self.driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option["+str(puntoVenta) +"]")
            pto = punto.get_attribute("value")
            if pto.find(puntoDeVenta) >= 0:
                punto.click()
                break
        
        if tipoComprobante == "10":
            tipo = self.driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table/tbody/tr[3]/td/div/select/option[1]").click()
        else:
            for tipoComp in range(1, 20):
                tipo = self.driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table/tbody/tr[3]/td/div/select/option["+str(tipoComp) +"]")
                t = tipo.get_attribute("value")
                if t.find(tipoComprobante) >= 0:
                    tipo.click()
                    break

        self.driver.find_element_by_xpath("/html/body/div[2]/form/input[2]").click()

    
    

    def consultas(self):
        self.driver.find_element_by_id("btn_consultas").click()
        sleep(3)

    def definirFechas(self):
        self.driver.find_element_by_id("fed").clear
        self.driver.find_element_by_id("fed").send_keys("01/01/2021")
        self.driver.find_element_by_id("feh").clear
        self.driver.find_element_by_id("feh").send_keys("31/01/2021")
        self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td/input[2]").click()

    def definirPuntoVenta(self):
        self.driver.find_element_by_id("puntodeventa")

    def exportarVentas(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/input[3]").click()

    def descargarVentas(self, username, password):
        Afip.Inicio(self)
        Afip.login(self, username, password)
        Afip.buscarMenu(self, "Comprobantes en línea")
        self.empresa("FOOD CORNER")
        self.consultas()
        self.definirFechas()
        self.exportarVentas()
        Afip.cerrar(self)

    def generarComprobante(self, username, password):
        Afip.Inicio(self)
        Afip.login(self, username, password)
        Afip.buscarMenu(self, "Comprobantes en línea")
        self.empresa("FOOD CORNER")
        self.generarComprobantes("101", "10")



compEnLinea = CompEnLinea()
compEnLinea.generarComprobante("20184719968", "EStudio887")