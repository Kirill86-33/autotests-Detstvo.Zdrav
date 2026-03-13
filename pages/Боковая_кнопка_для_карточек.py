from pages.base_page import BasePage

class SideButton(BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'

    BUTTON_SIDE = ("xpath", "//div[@class='slick-arrow slick-next']")
   
 
  
    def click_button_side (self):  
        button_side = self.driver.find_element(*self.BUTTON_SIDE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_side)