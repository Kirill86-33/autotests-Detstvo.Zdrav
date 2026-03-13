from pages.base_page import BasePage

class CardFirstAid(BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'


    CARD_FIRST_AID = ("xpath","//div//h4[text()='Первая помощь']") 
    BUTTON_TAB = ("xpath", "//div//h4[text()='Укусы животных']")



    def click_cart_first (self):  
        cart_first= self.driver.find_element(*self.CARD_FIRST_AID) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_first)


    def click_button_tab(self):  
        button_tab= self.driver.find_element(*self.BUTTON_TAB) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tab)