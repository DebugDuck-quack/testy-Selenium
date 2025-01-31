# testy-Selenium
Automatyczne testy aplikacji e-commerce-analizowanie dynamicznych elementów na stronie oraz generowanie raportu wyników
<br> 
<br> 

Wymagania:
<br> 
<br> 
-Google Chrome
<br> 
-WebDriver zgodny z wersją Chroma >>> https://googlechromelabs.github.io/chrome-for-testing/ należy umieścić w folderze /drivers
<br> 
-Selenium
<br> 
-pytest
<br> 
-pytest-html
<br> 
<br> 
Uruchomienie metody:
<br> 
<br> 
-Bezpośrednio z użyciem pliku bat 
<br> 
-Wywołanie z terminala 'pytest --html=reports/Report_TEST_RESULTS.html'
<br> 
<br> 
Uzyskane wyniki:
<br> 
WYNIKI PYTEST-HTML>>>
<br> 
![Rezultaty testów z pytest-html](Images/Report_TEST_RESULTS.png)
<br>  
OKNO PYTEST>>>
<br> 
![Okno pytest](Images/Tests_Running.png)
<br> 
<br> 
<br>
Aby zademonstrować obsługę błędów, dodałem przykład testu aby celowo zakończył się niepowodzeniem. W tym przypadku zmieniłem login na "Janusz", co spowodowało, że test `test_login_success` zakończył się błędem. Pozostałe testy zostały wykonane prawidłowo.Na poniższym screenie widać błąd asercji, który łatwo można zdiagnozować jako przyczynę błędu czyli nieprawidłowy login "Janusz" powoduje, że logowanie nie jest pomyślne:
<br> 
<br> 
WYNIKI PYTEST-HTML>>>
![Rezultaty testów z pytest-html](Images/Report_TEST_RESULTS_with_errors_login.png)
<br>  
OKNO PYTEST>>>
<br> 
![Okno pytest](Images/Tests_Running_with_errors_login.png)

