from pages.base_page import BasePage

class ConsultationPage(BasePage):
    PAGE_URL = 'https://detstvo.zdrav.mosreg.ru/'

    BUTTON_CONSULTATION = ("xpath", "(//div//h4[text()='Онлайн-консультация детского врача'])[1]")
    
 
  
    def click_button_consultation (self):  
       button_consultation = self.driver.find_element(*self.BUTTON_CONSULTATION) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_consultation)



   