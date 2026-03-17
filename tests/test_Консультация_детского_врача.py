from testit_python_commons.decorators import externalId, displayName
class TestConsultationPage:
    
    @externalId("test_consultation")
    @displayName("Консультация детского врача")
    def test_consultation(self, card_consuultation_page):  # Фикстура автоматически передаст login_page
        card_consuultation_page.open()
        card_consuultation_page.click_button_consultation()
