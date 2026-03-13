class TestChildrenPage:
    
    def test_children (self, card_children_health):  # Фикстура автоматически передаст login_page
        card_children_health.open()
        card_children_health.click_cart_children()
        card_children_health.click_button_tab()