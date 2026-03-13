class TestSideButton:
    
    def test_side_button(self, side_button):  # Фикстура автоматически передаст login_page
        side_button.open()
        side_button.click_button_side ()
        side_button.click_button_side ()
        side_button.click_button_side ()