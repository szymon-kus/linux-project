import psutil
import platform
import time
import os
import socket
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("encryption_key.key", "rb").read()

if not os.path.exists("encryption_key.key"):
    generate_key()

cipher_suite = Fernet(load_key())


def get_system_info():
    system_info = {
        'System': platform.system(),
        'Nazwa': platform.node(),
        'Wydanie': platform.release(),
        'Wersja': platform.version(),
        'Procesor': platform.processor(),
    }
    return system_info

def check_internet_connection():
    remote_server = "www.google.com"
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((remote_server, port))
        print("Internet is connected.")
        return True
    except socket.error:
        print("Internet is not connected.")
        return False
    finally:
        sock.close()


def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return {
        'Całkowita pojemność dysku': round(disk_usage.total / (1024 ** 3), 2),
        'Używana przestrzeń dyskowa (GB)': round(disk_usage.used / (1024 ** 3), 2),
        'Wolna przestrzeń dyskowa (GB)': round(disk_usage.free / (1024 ** 3), 2),
        'Procentowe zużycie dysku': disk_usage.percent,
    }

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return {'Procentowe zużycie procesora': cpu_usage}

def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        'Całkowita pojemność RAM (GB)': round(memory.total / (1024 ** 3), 2),
        'Używana pamięć RAM (GB)': round(memory.used / (1024 ** 3), 2),
        'Wolna pamięć RAM (GB)': round(memory.available / (1024 ** 3), 2),
        'Procentowe zużycie RAM': memory.percent,
    }

def display_system_info():
    print("\nInformacje o systemie:")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

def display_disk_usage():
    print("\nZużycie dysku:")
    for key, value in get_disk_usage().items():
        print(f"{key}: {value}")

def display_cpu_usage():
    print("\nZużycie procesora:")
    for key, value in get_cpu_usage().items():
        print(f"{key}: {value}")

def display_memory_usage():
    print("\nZużycie pamięci:")
    for key, value in get_memory_usage().items():
        print(f"{key}: {value}")

def save_to_file(data):
    with open("system_data.txt", "a") as file:
        file.write(data + "\n")

def check_updates():
    system_type = platform.system().lower()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    data_to_save = f"{timestamp}\n"

    print("Sprawdzanie aktualizacji Red Hat lub CentOS...")
    data_to_save += "Sprawdzanie aktualizacji systemowych...\n"

    if system_type == "linux":
        if os.path.exists("/etc/redhat-release"):
            print("Sprawdzanie aktualizacji Red Hat lub CentOS...")
            data_to_save += "Sprawdzanie aktualizacji Red Hat lub CentOS...\n"
            update_info = os.popen("yum check-update").read()
            data_to_save += f"Ostatnie sprawdzenie aktualizacji systemowych:\n{update_info}"
        elif os.path.exists("/etc/debian_version"):
            print("Sprawdzanie aktualizacji Red Hat lub CentOS...")
            data_to_save += "Sprawdzanie aktualizacji Red Hat lub CentOS...\n"
            update_info = os.popen("apt list --upgradable").read()
            data_to_save += f"Ostatnie sprawdzenie aktualizacji systemowych:\n{update_info}"

    save_to_file(data_to_save)

def save_to_external_file(data, filename):
    with open(filename, "a") as file:
        file.write(data + "\n")

def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            encrypted_data = cipher_suite.encrypt(data)

        with open(file_path + '.enc', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"Plik {file_path} został zaszyfrowany.")
    except Exception as e:
        print(f"Błąd podczas szyfrowania pliku {file_path}: {e}")

def display_menu():
    while True:
        print("\nMenu:")
        print("1. Wyświetl informacje o systemie")
        print("2. Wyświetl informacje o zużyciu dysku")
        print("3. Wyświetl informacje o zużyciu procesora")
        print("4. Wyświetl informacje o zużyciu pamięci")
        print("5. Sprawdź połączenie internetowe")
        print("6. Sprawdź aktualizacje systemowe")
        print("7. Zapisz dane do zewnętrznego pliku")
        print("0. Zakończ program")
        
        choice = int(input("Wybierz opcję: "))

        if choice == 1:
            display_system_info()
        elif choice == 2:
            display_disk_usage()
        elif choice == 3:
            display_cpu_usage()
        elif choice == 4:
            display_memory_usage()
        elif choice == 5:
            check_internet_connection()
        elif choice == 6:
            check_updates()
        elif choice == 7:
            filename = input("Podaj nazwę pliku do zapisu: ")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            data_to_save = f"{timestamp}\n"
            data_to_save += f"{get_system_info()}\n"
            data_to_save += f"{get_disk_usage()}\n"
            data_to_save += f"{get_cpu_usage()}\n"
            data_to_save += f"{get_memory_usage()}\n"
            save_to_external_file(data_to_save, filename)
            print(f"Dane zapisane do pliku: {filename}")

            encrypt_option = input("Czy chcesz zaszyfrować ten plik? (Tak/Nie): ").lower()
            if encrypt_option == 'tak':
                encrypt_file(filename)
    
        elif choice == 0:
            print("Zakończono program.")
            return
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def main():
    display_menu()

if __name__ == "__main__":
    main()