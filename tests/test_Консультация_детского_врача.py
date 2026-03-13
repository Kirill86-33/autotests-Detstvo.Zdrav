class TestConsultationPage:
    
    def test_consultation(self, card_consuultation_page):  # Фикстура автоматически передаст login_page
        card_consuultation_page.open()
        card_consuultation_page.click_button_consultation()
