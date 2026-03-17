from testit_python_commons.decorators import externalId, displayName

class TestSocialPage:
    
    @externalId("test_social_page")
    @displayName("Раздел Социальная поддержка")
    def test_social_page (self, card_social_support):  # Фикстура автоматически передаст login_page
        card_social_support.open()
        card_social_support.click_cart_social_spport()
        card_social_support.click_button_tab()