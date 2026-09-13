import sys

def sorgula():
    aranan = input("Aranacak kullanıcı adı: ").strip().lower()
    
    try:
        with open("login_logs.txt", "r", encoding="utf-8") as f:
            bulundu = False
            print(f"\n--- '@{aranan}' İçin Giriş Geçmişi ---")
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    user, pwd, zaman = parts
                    if user.lower() == aranan:
                        print(f"Zaman: {zaman} | Şifre: {pwd}")
                        bulundu = True
            if not bulundu:
                print("Bu kullanıcı adına ait kayıt bulunamadı.")
    except FileNotFoundError:
        print("Henüz hiç log kaydı oluşturulmamış.")

if __name__ == "__main__":
    sorgula()

