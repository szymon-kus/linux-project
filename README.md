# Dokumentacja programu 
## Opis ogólny
Program jest narzędziem, które umożliwia użytkownikowi uzyskanie informacji na temat systemu operacyjnego oraz jego zasobów takich jak dysk, pamięć, procesor, oraz połączenie z Internetem. Program pozwala również na sprawdzenie aktualizacji systemowych oraz zapisywanie danych do plików, zarówno lokalnych jak i zewnętrznych. Zapisany plik można zaszyfrować z wykorzystaniem biblioteki Fernet. 

## Instrukcja obsługi
Wymagania
Program działa na systemie operacyjnym Linux (pracowałem na Red Hat Enterprise Linux 9). Wymaga zainstalowanego interpretera Python 3 oraz pakietów psutil oraz cryptography.

generate_key()
Generuje nowy klucz szyfrowania i zapisuje go do pliku encryption_key.key.

load_key()
Wczytuje klucz szyfrowania z pliku encryption_key.key.

get_system_info()
Zwraca słownik z informacjami o systemie operacyjnym, takimi jak nazwa systemu, nazwa hosta, wydanie, wersja i procesor.

check_internet_connection()
Sprawdza połączenie z Internetem, łącząc się z serwerem Google'a na porcie 80.

get_disk_usage()
Zwraca informacje o zużyciu dysku, takie jak całkowita pojemność dysku, używana przestrzeń, wolna przestrzeń i procentowe zużycie dysku.

get_cpu_usage()
Zwraca informacje o procentowym zużyciu procesora.

get_memory_usage()
Zwraca informacje o zużyciu pamięci RAM, takie jak całkowita pojemność RAM, używana przestrzeń, wolna przestrzeń i procentowe zużycie pamięci.

display_system_info()
Wyświetla informacje o systemie operacyjnym, nazwie hosta, wydaniu, wersji i procesorze.

display_disk_usage()
Wyświetla informacje o zużyciu dysku, takie jak całkowita pojemność dysku, używana przestrzeń, wolna przestrzeń i procentowe zużycie dysku.

display_cpu_usage()
Wyświetla informacje o procentowym zużyciu procesora.

display_memory_usage()
Wyświetla informacje o zużyciu pamięci RAM, takie jak całkowita pojemność RAM, używana przestrzeń, wolna przestrzeń i procentowe zużycie pamięci.

save_to_file(data)
Zapisuje dane do pliku system_data.txt.

check_updates()
Sprawdza aktualizacje dla systemu operacyjnego i zapisuje dane do pliku system_data.txt.

save_to_external_file(data, filename)
Zapisuje dane do zewnętrznego pliku o podanej nazwie.

encrypt_file(file_path)
Szyfruje plik za pomocą klucza szyfrowania i zapisuje go jako plik z rozszerzeniem .enc.

display_menu()
Wyświetla menu główne programu i obsługuje wybór użytkownika, wykonując odpowiednie funkcje na podstawie wyboru.

main()
Główna funkcja programu, która uruchamia menu.

## Szyfrowanie plików
Program umożliwia szyfrowanie plików za pomocą klucza szyfrowania. Po szyfrowaniu plików, otrzymujemy plik z rozszerzeniem .enc.

## Zapisywanie danych do plików
Program umożliwia zapisywanie danych do pliku system_data.txt oraz do zewnętrznych plików o podanej przez użytkownika nazwie.
