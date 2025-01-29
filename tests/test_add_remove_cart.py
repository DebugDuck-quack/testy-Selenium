from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def setup_driver():
    
    # Inicjalizacja WebDrivera
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    return driver

def login(driver, username="standard_user", password="secret_sauce"):
    
    print("1. Wejście na stronę logowania -> https://www.saucedemo.com")
    driver.get("https://www.saucedemo.com")
    
    print(f"2. Wpisanie nazwy użytkownika -> {username}")
    driver.find_element(By.ID, "user-name").send_keys(username)
    
    print(f"3. Wpisanie hasła -> {password}")
    driver.find_element(By.ID, "password").send_keys(password)
    
    print("4. Kliknięcie przycisku -> LOGIN")
    driver.find_element(By.ID, "login-button").click()

def test_add_to_cart():
    
    # Test dodawania produktu do koszyka
    driver = setup_driver()
    try:
        print("PRZYPADEK TESTOWY >>> *DODANIE PRODUKTU DO KOSZYKA*")
        print()
        
        login(driver)
                
        print("5. Dodanie produktu-> 'Sauce Labs Backpack' do koszyka")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        print("6. Sprawdzenie, czy produkt został dodany do koszyka")
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == "1", f"Błąd!W koszyku powinna znajdować się następująca ilość produktów: 1 , ale otrzymano wynik: '{cart_badge}'"
        
        print()
        print("TEST DODAWANIA DO KOSZYKA - zakończony sukcesem!")
                
    finally:
        driver.quit()

def test_remove_from_cart():
    
    # Test usuwania produktu z koszyka
    driver = setup_driver()
    try:
        print("PRZYPADEK TESTOWY >>> *USUNIĘCIE PRODUKTU Z KOSZYKA*")
        print()
        
        login(driver)
        
        print("5. Dodanie produktu 'Sauce Labs Backpack' do koszyka")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        print("6. Usunięcie produktu z koszyka")
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        
        print("7. Sprawdzenie, czy koszyk jest pusty")
        cart_badge_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(cart_badge_elements) == 0, "Błąd!Koszyk powinien być pusty, ale nie jest."
        
        print()
        print("TEST USUWANIA Z KOSZYKA - zakończony sukcesem!")
        
    finally:
        driver.quit()