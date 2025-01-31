from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def setup_driver():
    # Inicjalizacja WebDrivera
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    return driver

def login(driver, username, password):

    
    print("1. Wejście na stronę logowania -> https://www.saucedemo.com")
    driver.get("https://www.saucedemo.com")
    
    print(f"2. Wpisanie nazwy użytkownika -> {username}")
    driver.find_element(By.ID, "user-name").send_keys(username)
    
    print(f"3. Wpisanie hasła -> {password}")
    driver.find_element(By.ID, "password").send_keys(password)
    
    print("4. Kliknięcie przycisku -> LOGIN")
    driver.find_element(By.ID, "login-button").click()

def test_login_success():
    
    # Test poprawnego logowania
    print("PRZYPADEK TESTOWY >>> *TEST POPRAWNEGO LOGOWANIA*")
    print()
    
    driver = setup_driver()
    try:
        login(driver, "standard_user", "secret_sauce")

        #sprawdzenie niepoprawnych danych logowania dla testu z prawidłowym logowaniem-wymuszenie błędu w tescie
        #login(driver, "Janusz", "secret_sauce")
        
        print("5. Sprawdzenie, czy użytkownik został przekierowany do strony inventory")
        assert "inventory" in driver.current_url, "Błąd!Logowanie nieudane!"
        
        print()        
        print("TEST POPRAWNEGO LOGOWANIA - zakończony sukcesem!")
    finally:
        driver.quit()

def test_login_fail():
    
    # Test niepoprawnego logowania
    print("PRZYPADEK TESTOWY >>> *TEST NIEPOPRAWNEGO LOGOWANIA*")
    print()
    
    driver = setup_driver()
    try:
        login(driver, "Prezes", "pass4321")
        
        print("5. Sprawdzenie komunikatu o błędzie logowania")
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username and password do not match" in error_message, "Błąd!Brak monitu błędnego logowania po wpisaniu niepoprawnych danych!"
        
        print() 
        print("TEST BŁĘDNEGO LOGOWANIA - zakończony sukcesem!")
    finally:
        driver.quit()

