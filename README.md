# Dokumentacja programu 
## Opis ogólny
Program jest narzędziem, które umożliwia użytkownikowi uzyskanie informacji na temat systemu operacyjnego oraz jego zasobów takich jak dysk, pamięć, procesor, oraz połączenie z Internetem. Program pozwala również na sprawdzenie aktualizacji systemowych oraz zapisywanie danych do plików, zarówno lokalnych jak i zewnętrznych. Zapisany plik można zaszyfrować z wykorzystaniem biblioteki Fernet. 

## Instrukcja obsługi
Wymagania
Program działa na systemie operacyjnym Linux (pracowałem na Red Hat Enterprise Linux 9). Wymaga zainstalowanego interpretera Python 3 oraz pakietów psutil oraz cryptography.

## Uruchomienie
Aby uruchomić program, należy wywołać skrypt Pythona w terminalu:

Copy code
python3 system_program.py
Po uruchomieniu programu użytkownikowi wyświetla się menu główne, z którego może wybrać opcje.

## Menu
Wyświetl informacje o systemie - Wyświetla informacje o systemie operacyjnym, wersji, nazwie hosta oraz procesorze.
Wyświetl informacje o zużyciu dysku - Wyświetla informacje o zużyciu dysku, w tym całkowitą pojemność dysku, używaną przestrzeń, wolną przestrzeń oraz procentowe zużycie dysku.
Wyświetl informacje o zużyciu procesora - Wyświetla informacje o procentowym zużyciu procesora.
Wyświetl informacje o zużyciu pamięci - Wyświetla informacje o pamięci RAM, w tym całkowitą pojemność RAM, używaną przestrzeń, wolną przestrzeń oraz procentowe zużycie pamięci.
Sprawdź połączenie internetowe - Sprawdza połączenie z Internetem.
Sprawdź aktualizacje systemowe - Sprawdza aktualizacje dla systemu operacyjnego.
Zapisz dane do zewnętrznego pliku - Zapisuje informacje o systemie do pliku o podanej nazwie.
Funkcje dodatkowe
Generowanie i ładowanie klucza
Program generuje klucz szyfrowania podczas pierwszego uruchomienia i zapisuje go do pliku encryption_key.key. Następnie klucz ten jest używany do szyfrowania i deszyfrowania danych.

## Szyfrowanie i deszyfrowanie plików
Program umożliwia szyfrowanie i deszyfrowanie plików za pomocą klucza szyfrowania. Po szyfrowaniu plików, otrzymujemy plik z rozszerzeniem .enc.

## Zapisywanie danych do plików
Program umożliwia zapisywanie danych do pliku system_data.txt oraz do zewnętrznych plików o podanej przez użytkownika nazwie.

## Zabezpieczenia
Program nie posiada wbudowanych zabezpieczeń na poziomie kodu źródłowego. Aby zapewnić bezpieczeństwo danych, należy odpowiednio zabezpieczyć dostęp do plików klucza szyfrowania, jak również ograniczyć dostęp do plików logów oraz plików systemowych.
