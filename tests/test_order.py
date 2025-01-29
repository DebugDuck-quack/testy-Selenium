from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



def setup_driver():
    
    #Inicjalizacja WebDrivera
    
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  
    return driver

def login(driver, username="standard_user", password="secret_sauce"):
    
    print("PRZYPADEK TESTOWY >>> *PROCES ZŁOŻENIA ZAMÓWIENIA*")
    print()
    
    #Logowanie na stronie testów- https://www.saucedemo.com
    
    print("1.Wejście na stronę logowania-> https://www.saucedemo.com")
    driver.get("https://www.saucedemo.com")
    
    print("2.Wpisanie nazwy użytkownika-> standard_user")
    driver.find_element(By.ID, "user-name").send_keys(username)
    
    print("3.Wpisanie hasła-> secret_sauce")
    driver.find_element(By.ID, "password").send_keys(password)
    
    print("4.Kliknięcie przycisku-> LOGIN")
    driver.find_element(By.ID, "login-button").click()

def test_order_process():
    
    #Test procesu zamówienia
    
    driver = setup_driver()
    try:
        login(driver)
        
        print("5.Dodanie produktu 'Sauce Labs Backpack' do koszyka-> kliknięcie przycisku ADD TO CART")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        print("6.Przejście do koszyka-> kliknięcie przycisku koszyka")
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        print("7.Rozpoczęcie procesu finalizacji zamówienia->kliknięcie przycisku CHECKOUT")
        driver.find_element(By.ID, "checkout").click()
        
        print("8.Wprowadzenie danych użytkownika-> imię, nazwisko, kod pocztowy")
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Rambo")
        driver.find_element(By.ID, "postal-code").send_keys("121541")
        
        print("9.Potwierdzenie wpisanych danych-> kliknięcie przycisku CONTINUE")
        driver.find_element(By.ID, "continue").click()
        
        print("10.Zakończenie-> kliknięcie przycisku FINISH")
        driver.find_element(By.ID, "finish").click()

                
        print("11.Sprawdzenie komunikatu potwierdzającego zamówienie")
        confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you for your order!" in confirmation, "Błąd w asercji komunikatu potwierdzającego!"
        print()
        print("TEST PROCESU ZŁOŻENIA ZAMÓWIENIA- zakończony sukcesem!")
    finally:
        driver.quit()
