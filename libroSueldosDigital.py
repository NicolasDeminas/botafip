from selenium import webdriver
from time import sleep
from Afip import Afip
import paths.paths as paths

class LibroSueldos:
    def inicio(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)

    def menuConsultas(self):
        self.driver.find_element_by_xpath("/html/body/form/div[3]/div[5]/div[2]/div[3]/a").click()

    def periodo(self, periodo):
        self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_InputPeriodo1_txtPeriodo").send_keys(periodo)
        self.driver.find_element_by_xpath("/html/body/form/div[3]/div[6]/div[3]/div[2]/input").click()

    def descargarArchivos(self):
            for c in range(2, 20):
                try:
                    liquidacion = self.driver.find_element_by_xpath("/html/body/form/div[3]/div[6]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[" + str(c) + "]/td[5]/input")
                    liquidacion.click()
                except Exception:
                    break


    def libroSueldosDigital(self, username, password, periodo):
        Afip.Inicio(self)
        Afip.login(self, username, password)
        Afip.buscarMenu(self, "Libro de Sueldos Digital")
        self.menuConsultas()
        self.periodo(periodo)
        self.descargarArchivos()
        Afip.cerrar(self)

