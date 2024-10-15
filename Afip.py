from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import paths.paths as paths

#Clase para inicializar el ingreso en pagina de AFIP
class Afip:
    def Inicio(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")
    
    #Las referencias estan en el archivo paths, y en Secret los datos de ingreso 
    def login(self, username, password):
        # self.driver.find_element_by_name(paths.ingresar_usuario).send_keys(username)
        # self.driver.find_element_by_name(paths.ingresar_usuario_boton).click()
        # self.driver.find_element_by_name(paths.ingresar_contraseña).send_keys(password)
        # self.driver.find_element_by_name(paths.ingresar_contraseña_boton).click()
        # self.driver.execute_script('window.localStorage.setItem("AFIPCOMUNICACIONENG", "true")')
        self.driver.find_element(By.NAME, paths.ingresar_usuario).send_keys(username)
        self.driver.find_element(By.NAME,paths.ingresar_usuario_boton).click()
        self.driver.find_element(By.NAME, paths.ingresar_contraseña).send_keys(password)
        self.driver.find_element(By.NAME, paths.ingresar_contraseña_boton).click()

    def changeMenu(self):
        # self.driver.find_element_by_xpath('/html/body/div/div/main/section[1]/div/ul/li[3]/a').click()
        # try:
        #     self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]').click()
        # except Exception as e:
        #     print(e)
            
        menu = self.driver.find_element(By.XPATH,'/html/body/div/div/main/section[1]/div/div/div/div[5]/div/a')
        self.driver.execute_script('arguments[0].scrollIntoView(true)', menu)
        menu.click()
        sleep(2)

    #Hace un loop for para encontrar el nombre del Menu dentro de la pagina de AFIP, dicho nombre se tiene que pasar
    #como parametro desde la clase que lo inicialice
    def buscarMenu(self, menu):
        
        for n in range(1, 200):
            try:
                # boton = self.driver.find_element_by_xpath(f"/html/body/div/div/main/div[2]/section[2]/div/div/div[{str(n)}]/div/div/div/div[2]/h4")
                boton = self.driver.find_element(By.XPATH,f"/html/body/div/div/main/div/section/div/div[3]/div[{str(n)}]/a/div/div/h3")
                # boton = self.driver.find_element_by_xpath(f"/html/body/div/div/main/div/section/div/div[3]/div[44]/a")
                

                if boton.text == menu.upper():
                    self.driver.execute_script('arguments[0].scrollIntoView(true)', boton)
                    sleep(1)
                    boton.click()
                    break
            except Exception as e:
                print(e)
                break
        sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        

    def cerrar(self):
        sleep(2)
        self.driver.quit()
    
