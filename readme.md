# librus-autologin

## Instalacja
1. Pobierz ten projekt używając zielonego przycisku w prawym górnym rogu strony > Download as ZIP.
2. Wypakuj ten projekt gdziekolwiek na twoim dysku (byle nie do kosza).
3. Zainstaluj Pythona w wersji 3 https://www.python.org/downloads/ Podczas instalacji zaznacz opcję Add Python to PATH.
4. Sprawdź wersję swojej przeglądarki Chrome.
```
3 kropki w prawym górnym rogu > Pomoc > Google Chrome - Informacje
```
5. Pobierz chromedriver w wersji odpowiadającej przeglądarce https://chromedriver.chromium.org/downloads
6. Wypakuj plik chromedriver z pobranego archiwum do katalogu w którym znajduje się ta instrukcja.
7. Otwórz cmd, przejdź do tego katalogu i zainstaluj dodatkowe biblioteki.
```
cd \twoja\sciezka
pip3 install -r requirements.txt
```
## Użycie
Otwórz cmd, przejdź do tego katalogu i uruchom program.
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
