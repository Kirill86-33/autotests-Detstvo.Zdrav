from testit_python_commons.decorators import externalId, displayName

class TestPolyclinicPage:
    
    @externalId("test_polyclinic")
    @displayName("Раздел Поликлиника и ребенок")
    def test_polyclinic (self, card_polyclinic):  # Фикстура автоматически передаст login_page
        card_polyclinic.open()
        card_polyclinic.click_cart_polyclinics()
        card_polyclinic.click_button_tab()