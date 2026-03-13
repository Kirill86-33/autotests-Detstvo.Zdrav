from pages.base_page import BasePage

class CardSocialSupport(BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'


    CARD_SOCIAL_SUPPORT = ("xpath","//div//h4[text()='Сoциальная пoддержка']") 
    BUTTON_TAB = ("xpath", "//div//h4[text()='Молочная кухня']")



    def click_cart_social_spport (self):  
        cart_social= self.driver.find_element(*self.CARD_SOCIAL_SUPPORT) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_social)


    def click_button_tab(self):  
        button_tab= self.driver.find_element(*self.BUTTON_TAB) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tab)