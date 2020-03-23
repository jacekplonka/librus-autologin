## Instalacja

    1. Zainstaluj Pythona w wersji 3 https://www.python.org/downloads/ Podczas instalacji zaznacz opcję Add Python to PATH
    2. Sprawdź wersję swojej przeglądarki Chrome
        ```
        3 kropki w prawym górnym rogu > Pomoc > Google Chrome - Informacje
        ```
    3. Pobierz chromedriver w wersji odpowiadającej przęglądarce https://chromedriver.chromium.org/downloads
    4. Wypakuj plik chromedriver z pobranego archiwum do katalogu w którym znajduje się ta instrukcja
    5. Otwórz cmd, przejdź do tego katalogu i zainstaluj dodatkowe biblioteki
        ```
        cd \twoja\sciezka
        pip3 install -r requirements.txt
        ```


## Uzycie

    Otwórz cmd, przejdź do tego katalogu i uruchom program
    ```
    cd \twoja\sciezka
    zaloguj.bat login hasło ile_razy_powtorzyc interwał_w_minutach
    ```

## Przykłady

    Powtórz logowanie co 60 minut, przez 6 godzin:
    ```
    zaloguj.bat kacper.pawel@gmail.com haslo2137 6 60
    ```

    Zaloguj się 2 razy w ciągu 6 godzin:
    ```
    zaloguj.bat kacper.pawel@gmail.com haslo2137 2 180
    ```