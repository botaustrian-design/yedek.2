import json
import os

DOSYA = "oyuncular.json"

def veri_oku():
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def bilgi_sorgula():
    veri = veri_oku()
    k_adi = input("Username: ")
    
    if k_adi in veri:
        bilgiler = veri[k_adi]
        print(f"\n--- Kullanıcı Bilgileri: {k_adi} ---")
        print(f"Password      : {bilgiler.get('sifre')}")
        print(f"Kayıt Tarihi  : {bilgiler.get('kayit_tarihi', 'Bilinmiyor')}")
        print(f"Son Giriş     : {bilgiler.get('son_giris', 'Bilinmiyor')}")
        print(f"Seviye        : {bilgiler.get('seviye', 1)}")
        print(f"Skor          : {bilgiler.get('skor', 0)}")
        print("-" * 30)
    else:
        print("Böyle bir kullanıcı bulunamadı.")

if __name__ == "__main__":
    bilgi_sorgula()
