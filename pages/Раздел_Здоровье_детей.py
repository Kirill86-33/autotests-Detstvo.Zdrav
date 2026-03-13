from pages.base_page import BasePage

class CardChildrenHealth(BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'


    CARD_CHILDREN = ("xpath","//div//h4[text()='Здоровье детей']") 
    BUTTON_TAB = ("xpath", "//div//h4[text()='Профилактика лактостаза']")



    def click_cart_children (self):  
        cart_children= self.driver.find_element(*self.CARD_CHILDREN) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_children)


    def click_button_tab(self):  
        button_tab= self.driver.find_element(*self.BUTTON_TAB) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tab)