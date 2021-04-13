from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import paths.paths as paths


class Afip:
    def Inicio(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(20)
        self.driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")
    

    def login(self, username, password):
        self.driver.find_element_by_name(paths.ingresar_usuario).send_keys(username)
        self.driver.find_element_by_name(paths.ingresar_usuario_boton).click()
        self.driver.find_element_by_name(paths.ingresar_contraseña).send_keys(password)
        self.driver.find_element_by_name(paths.ingresar_contraseña_boton).click()
   
    def buscarMenu(self, menu):
        for n in range(1, 200):
            try:
                boton = self.driver.find_element_by_xpath("/html/body/main/section[2]/div/div[" + str(n) + "]/div/div/div/div[2]/h4")
                #print(boton.text)
                if boton.text == menu:
                    #print(boton.text)
                    boton.click()
                    break
            except Exception:
                break
        sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        

    def cerrar(self):
        sleep(2)
        self.driver.quit()
    
