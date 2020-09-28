from selenium import webdriver
from time import sleep
from datetime import date, datetime, timedelta
import Secret

class BotAfip:
        
    def __init__(self,username,pw,fecha):
        path = "C:\Program Files (x86)/chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        # Ingreso a web AFIP
        self.driver.get("http://www.afip.gov.ar/sitio/externos/default.asp")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/a").click()
        ######sleep(3)
        # Carga de usuario
        self.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/div/form/div/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/div/form/input[2]").click() 
        sleep(1)
        # Ingreso de contraseña
        self.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]").send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/div/form/div/input[3]").click()
        sleep(1)
        # Seleccionar "Mis Comprobantes" - "Recibidos"
        self.driver.find_element_by_xpath("/html/body/main/section/div/div[43]/div/div/div/div[2]/h4").click()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("/html/body/main/div/section/div/div/div[3]/a").click()
        # Cargar el rango de fechas y buscar los comprobantes
        self.driver.find_element_by_xpath("/html/body/main/div/section/div/div/div[1]/div/div[1]/div/div/input").clear()
        self.driver.find_element_by_xpath("/html/body/main/div/section/div/div/div[1]/div/div[1]/div/div/input").send_keys(fecha)
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div/button[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/main/div/section/div/div/div[1]/div/div[5]/div/button").click()
        sleep(20)
        # Descargar la pantalla en formato CSV
        self.driver.find_element_by_xpath("/html/body/main/div/section/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/button[1]").click()
        sleep(3)

hoy = date.today()
mesAnterior = hoy - timedelta(days=31)

hoy = hoy.strftime("%d/%m/%Y")

mesAnterior = mesAnterior.strftime("%d/%m/%Y")
        
fecha = mesAnterior," - ",hoy
#print (fecha)    
BotAfip("20184719968", Secret.pw,fecha)    



