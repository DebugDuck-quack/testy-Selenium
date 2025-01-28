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
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def test_checkout_process():
    """Test finalizacji zamówienia"""
    driver = setup_driver()
    try:
        login(driver)  # Logowanie na konto
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()  # Dodanie produktu do koszyka
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()  # Przejście do koszyka
        driver.find_element(By.ID, "checkout").click()  # Rozpoczęcie procesu finalizacji
        driver.find_element(By.ID, "first-name").send_keys("John")  # Wprowadzenie danych
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()  # Zakończenie zamówienia

        # Sprawdzenie komunikatu potwierdzającego
        confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "THANK YOU FOR YOUR ORDER" in confirmation, "Zamówienie nie zostało zakończone poprawnie!"
        print("Test finalizacji zamówienia zakończony sukcesem!")
    finally:
        driver.quit()
