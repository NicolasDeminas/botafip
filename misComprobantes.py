from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Afip import Afip
import paths.paths as paths

# La clase se ocupa de manejar tanto el ingreso al menu de Mis Comprobantes, como de definir las fechas buscadas y la descarga
#del archivo CSV
class misComprobantes:
    def Iniciar(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)
    
    #La función se ejecuta siempre, aunque su resultado es opcional, dependiendo si el usuario tiene asignado el menu para 
    #mas de una empresa
    #La logica es similar a la de la busqueda del menu, haciendo un loop for buscando el nombre de la empresa, el cual debe
    #ser pasado como parametro al instancear el objeto
    def empresa(self, empresa:str):
        for n in range(1, 10):
            try:
                representar = self.driver.find_element(By.XPATH, "/html/body/form/main/div/div/div[2]/div/div[" + str(n) + "]/div/a")
                r = representar.text
                if r.find(empresa.upper()) >= 0:
                    self.driver.execute_script('arguments[0].scrollIntoView(true)', representar)
                    representar.click()
                    break
            except Exception:
                break

    def comprobantes(self, tipoComprobante:str):
        sleep(1)
        for c in range(2, 5):
            comp = self.driver.find_element(By.XPATH, "/html/body/main/div/section/div/div/div[" + str(c) + "]/a")
            compr = comp.text
            if compr.find(tipoComprobante.capitalize()) >= 0:
                comp.click()
                break
    
    def seleccionarComprobantes(self, fecha):
        self.driver.find_element(By.XPATH, paths.definir_fecha).clear()
        self.driver.find_element(By.XPATH, paths.definir_fecha).send_keys(fecha)
        self.driver.find_element(By.XPATH, paths.boton_aceptar_fecha).click()
        self.driver.execute_script('arguments[0].scrollIntoView(true)', self.driver.find_element(By.ID, paths.boton_buscar_comprobantes))
        self.driver.find_element(By.ID, paths.boton_buscar_comprobantes).click()
        
    def descargarCSV(self):
        sleep(20)
        self.driver.find_element(By.XPATH, paths.descargar_csv).click()


    def descargarComprobantes(self, username, password, empresa, tipoComprobante, dias):
        Afip.Inicio(self)
        Afip.login(self, username, password)
        Afip.changeMenu(self)
        Afip.buscarMenu(self, "Mis Comprobantes")
        self.empresa(empresa)
        self.comprobantes(tipoComprobante)
        self.seleccionarComprobantes(paths.fecha(dias))
        self.descargarCSV()
        Afip.cerrar(self)

