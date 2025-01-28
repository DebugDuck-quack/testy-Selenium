from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

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

def test_sort_products():
    """Test sortowania produktów według ceny"""
    driver = setup_driver()
    try:
        login(driver)  # Logowanie na konto
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.send_keys("Price (low to high)")
        sort_dropdown.send_keys(Keys.RETURN)  # Potwierdzenie wyboru

        # Sprawdzenie czy produkty są posortowane
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        price_values = [float(price.text.replace("$", "")) for price in prices]
        assert price_values == sorted(price_values), "Produkty nie są posortowane poprawnie!"
        print("Test sortowania produktów zakończony sukcesem!")
    finally:
        driver.quit()
