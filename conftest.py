import pytest
from selenium import webdriver
from pages.Поле_Поиск_Главная_страница import SearchField
from pages.Консультация_детского_врача import ConsultationPage
from pages.Боковая_кнопка_для_карточек import SideButton
from pages.Раздел_Первая_помощь import CardFirstAid
from pages.Раздел_Поликлиника_и_ребенок import CardPolyclinic
from pages.Раздел_Медицинские_услуги import CardMedicalServices
from pages.Раздел_Здоровье_детей import CardChildrenHealth
from pages.Раздел_Социальная_поддержка import CardSocialSupport
from pages.Раздел_Карьера_в_здравохранении import CardCareerHealth
from pages.Кнопка_Все_материалы_блок_Полезное import ButtonMaterials
from pages.Кнопка_Смотреть_все_блок_Все_новости import ButtonWatchAll
from pages.Поле_Поиск_блок_Полезное import SearchUsefulPage
from pages.Вкладка_Важное_блок_Полезное import TabImportant
from pages.Поле_Сортировка_блок_Полезное import SortingPage
from pages.Кнопка_Подписаться_блок_Все_новости import ButtonSubscribe
from pages.Поле_Поиск_Все_новости import SearchNewsPage
from pages.Тег_блок_Все_новости import TagNews





@pytest.fixture # Общие настройки экрана для всех фикстур
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def search_page(driver):
    return SearchField (driver)

@pytest.fixture
def card_consuultation_page(driver):
    return ConsultationPage (driver)


@pytest.fixture
def side_button(driver):
    return SideButton(driver)


@pytest.fixture
def card_first_aid(driver):
    return CardFirstAid(driver)


@pytest.fixture
def card_polyclinic(driver):
    return CardPolyclinic(driver)


@pytest.fixture
def card_medical_services(driver):
    return CardMedicalServices(driver)


@pytest.fixture
def card_children_health (driver):
    return CardChildrenHealth(driver)


@pytest.fixture
def card_social_support (driver):
    return CardSocialSupport (driver)


@pytest.fixture
def card_career_health (driver):
    return CardCareerHealth (driver)


@pytest.fixture
def button_all_materials (driver):
    return ButtonMaterials (driver)


@pytest.fixture
def button_watch_all (driver):
    return ButtonWatchAll (driver)

@pytest.fixture
def search_useful (driver):
    return SearchUsefulPage (driver)


@pytest.fixture
def button_tab_important (driver):
    return TabImportant (driver)


@pytest.fixture
def button_sorting (driver):
    return SortingPage (driver)


@pytest.fixture
def button_subscribe (driver):
    return ButtonSubscribe (driver)

@pytest.fixture
def search_news_page (driver):
    return SearchNewsPage (driver)

@pytest.fixture
def tag_news (driver):
    return TagNews (driver)