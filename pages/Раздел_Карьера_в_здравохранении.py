from pages.base_page import BasePage

class CardCareerHealth(BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'


    CARD_CAREER_HEALTH = ("xpath","//div//h4[text()='Карьера в здравоохранении']") 
    BUTTON_TAB = ("xpath", "//div//h4[text()='Медицинские классы']")



    def click_cart_career_health (self):  
        cart_career= self.driver.find_element(*self.CARD_CAREER_HEALTH) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_career)


    def click_button_tab(self):  
        button_tab= self.driver.find_element(*self.BUTTON_TAB) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tab)