class TestPolyclinicPage:
    
    def test_polyclinic (self, card_polyclinic):  # Фикстура автоматически передаст login_page
        card_polyclinic.open()
        card_polyclinic.click_cart_polyclinics()
        card_polyclinic.click_button_tab()