class TestMedicalPage:
    
    def test_medical_services (self, card_medical_services):  # Фикстура автоматически передаст login_page
        card_medical_services.open()
        card_medical_services.click_cart_medical_services()
        card_medical_services.click_button_tab()