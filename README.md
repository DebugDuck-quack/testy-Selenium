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
A teraz przykład gdzie celowo zmieniłem login aby uzyskać błąd testu (Login:"Janusz")
<br> Fail dla funkcji 'test_login_success'.Reszta testów wykonała sie prawidłowo

<br> 
![Rezultaty testów z pytest-html](Images/Report_TEST_RESULTS_with_errors_login.png)
<br>  
OKNO PYTEST>>>
<br> 
![Okno pytest](Images/Tests_Running_with_errors_login.png)