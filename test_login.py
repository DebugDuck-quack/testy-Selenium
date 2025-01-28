from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def setup_driver():
    """Inicjalizacja WebDrivera"""
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Czekaj maksymalnie 10 sekund na elementy
    return driver

def test_login_success():
    """Test poprawnego logowania"""
    driver = setup_driver()  # Inicjalizacja WebDrivera
    try:
        # Otwórz stronę testów
        driver.get("https://www.saucedemo.com")
        # Wprowadź dane logowania
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        # Sprawdzamy, czy użytkownik został przekierowany do strony inventory
        assert "inventory" in driver.current_url, "Logowanie nieudane!"
        print("Logowanie powiodło się!")
    finally:
        # Zamknięcie przeglądarki
        driver.quit()

def test_login_failure():
    """Test niepoprawnego logowania"""
    driver = setup_driver()  # Inicjalizacja WebDrivera
    try:
        # Otwórz stronę testów
        driver.get("https://www.saucedemo.com")
        # Wprowadź błędne dane logowania
        driver.find_element(By.ID, "user-name").send_keys("wrong_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login-button").click()
        # Sprawdź komunikat o błędzie
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username and password do not match" in error_message, "Brak monitu błędu logowania!"
        print("Test błędnego logowania zakończony pozytywnie.")
    finally:
        # Zamknięcie przeglądarki
        driver.quit()
