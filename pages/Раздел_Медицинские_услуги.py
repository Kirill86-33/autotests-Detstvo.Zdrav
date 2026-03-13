from pages.base_page import BasePage

class CardMedicalServices (BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'


    CARD_MEDICAL_SERVICES = ("xpath","//div//h4[text()='Медицинские услуги']") 
    BUTTON_TAB = ("xpath", "//div//h4[text()='Исследования']")



    def click_cart_medical_services(self):  
        cart_medical= self.driver.find_element(*self.CARD_MEDICAL_SERVICES) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_medical)



    def click_button_tab(self):  
        button_tab= self.driver.find_element(*self.BUTTON_TAB) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tab)