import json
import os

DOSYA = "oyuncular.json"

def veri_oku():
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def veri_yaz(veri):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

def kayit_ol():
    print("\n--- OYUNCU KAYIT ---")
    k_adi = input("Kullanıcı adı: ")
    veri = veri_oku()
    
    if k_adi in veri:
        print("Bu kullanıcı adı zaten alınmış!")
        return
        
    sifre = input("Şifre: ")
    veri[k_adi] = {"sifre": sifre, "skor": 0, "seviye": 1}
    veri_yaz(veri)
    print(f"'{k_adi}' başarıyla kaydedildi!")

def oyuncu_sorgula():
    print("\n--- OYUNCU BİLGİ SORGULAMA ---")
    k_adi = input("Aranacak kullanıcı adı: ")
    veri = veri_oku()
    
    if k_adi in veri:
        print(f"\nKullanıcı Bulundu:")
        print(f"Kullanıcı Adı: {k_adi}")
        print(f"Şifre: {veri[k_adi]['sifre']}")
        print(f"Skor: {veri[k_adi]['skor']}")
        print(f"Seviye: {veri[k_adi]['seviye']}")
    else:
        print("Böyle bir oyuncu bulunamadı.")

while True:
    print("\n1. Kayıt Ol")
    print("2. Oyuncu Bilgilerini Sorgula")
    print("3. Çıkış")
    secim = input("Seçiminiz (1/2/3): ")
    
    if secim == "1":
        kayit_ol()
    elif secim == "2":
        oyuncu_sorgula()
    elif secim == "3":
        break
    else:
        print("Geçersiz seçim.")
