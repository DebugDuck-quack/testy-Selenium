from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def setup_driver():
    """Inicjalizacja WebDrivera"""
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Czekaj maksymalnie 10 sekund na elementy
    return driver

def login(driver, username="standard_user", password="secret_sauce"):
    """Logowanie na stronę testów"""
    driver.get("https://www.saucedemo.com")  # Otwórz stronę
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def test_add_to_cart():
    """Test dodawania produktu do koszyka"""
    driver = setup_driver()  # Inicjalizacja WebDrivera
    try:
        login(driver)  # Logowanie z poprawnymi danymi
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == "1", f"Expected '1', but got '{cart_badge}'"
    finally:
        driver.quit()  # Zamknięcie przeglądarki

def test_remove_from_cart():
    """Test usuwania produktu z koszyka"""
    driver = setup_driver()  # Inicjalizacja WebDrivera
    try:
        login(driver)  # Logowanie z poprawnymi danymi
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()  # Dodanie produktu
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()  # Usunięcie produktu
        cart_badge_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(cart_badge_elements) == 0, "Koszyk powinien być pusty, ale tak nie jest."
    finally:
        driver.quit()  # Zamknięcie przeglądarki
