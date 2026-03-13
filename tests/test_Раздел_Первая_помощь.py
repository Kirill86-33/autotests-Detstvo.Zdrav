class TestFirstPage:
    
    def test_first_aid (self, card_first_aid):  # Фикстура автоматически передаст login_page
        card_first_aid.open()
        card_first_aid.click_cart_first()
        card_first_aid.click_button_tab()