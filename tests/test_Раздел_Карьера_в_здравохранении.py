from testit_python_commons.decorators import externalId, displayName

class TestCareerPage:
    
    @externalId("test_career_health")
    @displayName("Раздел Карьера в здравоохранении")
    def test_career_health (self, card_career_health):  # Фикстура автоматически передаст login_page
        card_career_health.open()
        card_career_health.click_cart_career_health()
        card_career_health.click_button_tab()