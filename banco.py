from selenium import webdriver
import paths
import Secret


class Banco:
    def Inicio(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(10)
        self.driver.get(paths.galicia)

    def login(self, username, password):
        self.driver.find_element_by_class_name('office_banking').click()
        self.driver.find_element_by_id('UserID').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submitButton').click()

    def buscar_mes(self, fecha_desde, fecha_hasta):
        self.driver.find_element_by_xpath('/html/body/div[3]/section/div[2]/div[7]/table/tbody[2]/tr[1]').click()
        self.driver.find_element_by_id('fechaDesde').clear()
        self.driver.find_element_by_id('fechaDesde').send_keys(fecha_desde)
        self.driver.find_element_by_id('fechaHasta').clear()
        self.driver.find_element_by_id('fechaHasta').send_keys(fecha_hasta)
        self.driver.find_element_by_id('consultarCC').click()
        self.driver.find_element_by_id('expoOnline').click()
        self.driver.find_element_by_class_name('csv').click()

    def ingresarGalicia(self, username, password, fecha_desde, fecha_hasta):
        self.Inicio()
        self.login(username, password)
        self.buscar_mes(fecha_desde, fecha_hasta)

    
fechas = paths.fechas_mes()

galicia = Banco()
galicia.ingresarGalicia(Secret.galicia_username_food, Secret.galicia_password_food, fechas[0], fechas[1])

