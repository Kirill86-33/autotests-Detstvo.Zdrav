from testit_python_commons.decorators import externalId, displayName

class TestMedicalPage:
    
    @externalId("test_medical_services")
    @displayName("Раздел Медицинские услуги")
    def test_medical_services (self, card_medical_services):  # Фикстура автоматически передаст login_page
        card_medical_services.open()
        card_medical_services.click_cart_medical_services()
        card_medical_services.click_button_tab()