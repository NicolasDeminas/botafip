from selenium import webdriver
from time import sleep
from Afip import Afip
import paths.paths as paths

class LibroSueldos:
    def inicio(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)

    def menuConsultas(self, empresa):
        #Agregar un Try/Except y un loop for para seleccionar la empresa en caso de haber más de una
        for n in range(1, 10):
            try:
                self.driver.find_element_by_id("ddlCUIT").click()
                representar = self.driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/table/tbody/tr[2]/td/select/option["+str(n)+"]")
                r = representar.text
                if r.find(empresa) >= 0:
                    representar.click()
                    break
                self.driver.find_element_by_id("btnAceptar").click()
            except Exception:
                break
        
        #self.driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/table/tbody/tr[2]/td/select/option[1]").click()
        #self.driver.find_element_by_id("btnAceptar").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/form/div[3]/div[5]/div[2]/div[3]/a").click()

    def periodo(self, periodo):
        self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_InputPeriodo1_txtPeriodo").send_keys(periodo)
        self.driver.find_element_by_xpath("/html/body/form/div[3]/div[6]/div[4]/div[2]/input").click()

    def descargarArchivos(self):
            for c in range(2, 20):
                try:
                    liquidacion = self.driver.find_element_by_xpath("/html/body/form/div[3]/div[6]/div[4]/table/tbody/tr[2]/td/table/tbody/tr[" + str(c) + "]/td[5]/input")                                    
                    liquidacion.click()
                except Exception:
                    break


    def libroSueldosDigital(self, username, password, periodo, empresa):
        Afip.Inicio(self)
        Afip.login(self, username, password)
        Afip.changeMenu(self)
        Afip.buscarMenu(self, "Libro de Sueldos Digital")
        self.menuConsultas(empresa)
        self.periodo(periodo)
        self.descargarArchivos()
        Afip.cerrar(self)

