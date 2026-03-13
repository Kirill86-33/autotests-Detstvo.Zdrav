from pages.base_page import BasePage

class CardPolyclinic(BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'


    CARD_POLYCLINIC = ("xpath","//div//h4[text()='Поликлиника и ребёнок']") 
    BUTTON_TAB = ("xpath", "//div//h4[text()='Оформить полис ОМС']")



    def click_cart_polyclinics (self):  
        cart_polyclinics= self.driver.find_element(*self.CARD_POLYCLINIC) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_polyclinics)


    def click_button_tab(self):  
        button_tab= self.driver.find_element(*self.BUTTON_TAB) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tab)