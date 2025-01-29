from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

def setup_driver():
    # Inicjalizacja WebDrivera
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    return driver

def login(driver, username="standard_user", password="secret_sauce"):
    print("PRZYPADEK TESTOWY >>> *SORTOWANIE PRODUKTÓW*")
    print()
    
    print("1. Wejście na stronę logowania -> https://www.saucedemo.com")
    driver.get("https://www.saucedemo.com")
    
    print(f"2. Wpisanie nazwy użytkownika -> {username}")
    driver.find_element(By.ID, "user-name").send_keys(username)
    
    print(f"3. Wpisanie hasła -> {password}")
    driver.find_element(By.ID, "password").send_keys(password)
    
    print("4. Kliknięcie przycisku -> LOGIN")
    driver.find_element(By.ID, "login-button").click()

def test_sort_products():
    # Test sortowania produktów według ceny
    driver = setup_driver()
    try:
        login(driver)
        
        print("5. Wybór opcji sortowania -> 'Price (low to high)'")
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.send_keys("Price (low to high)")
        sort_dropdown.send_keys(Keys.RETURN)
        
        print("6. Pobranie cen produktów z listy")
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        price_values = [float(price.text.replace("$", "")) for price in prices]
        
        print("7. Sprawdzenie poprawności sortowania")
        assert price_values == sorted(price_values), "Błąd: Produkty nie zostały posortowane poprawnie!"
        
        print()        
        print("TEST SORTOWANIA PRODUKTÓW - zakończony sukcesem!")
    finally:
        driver.quit()
