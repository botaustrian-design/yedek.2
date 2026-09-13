from flask import Flask, render_template_string, request
import json
import os
from datetime import datetime

app = Flask(__name__)
DOSYA = "oyuncular.json"

def veri_oku():
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def veri_yaz(veri):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

HTML_SAYFA = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Oyun Paneli</title>
    <style>
        body { font-family: Arial, sans-serif; background: #121212; color: #fff; text-align: center; padding: 50px; }
        form { background: #1e1e1e; padding: 20px; display: inline-block; border-radius: 8px; }
        input { display: block; margin: 10px auto; padding: 10px; width: 200px; border-radius: 4px; border: none; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; margin: 5px; }
        .msg { color: #ffeb3b; margin-top: 15px; }
    </style>
</head>
<body>
    <h2>Oyun Kayıt ve Giriş Paneli</h2>
    <form method="POST">
        <input type="text" name="k_adi" placeholder="Kullanıcı Adı" required>
        <input type="password" name="sifre" placeholder="Şifre" required>
        <button type="submit" name="islem" value="kayit">Kayıt Ol</button>
        <button type="submit" name="islem" value="giris">Giriş Yap</button>
    </form>
    {% if mesaj %}
        <p class="msg">{{ mesaj }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    veri = veri_oku()
    mesaj = ""
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if request.method == "POST":
        k_adi = request.form.get("k_adi")
        sifre = request.form.get("sifre")
        islem = request.form.get("islem")
        
        if islem == "kayit":
            if k_adi in veri:
                mesaj = "Bu kullanıcı adı zaten alınmış!"
            else:
                veri[k_adi] = {
                    "sifre": sifre, 
                    "kayit_tarihi": zaman, 
                    "son_giris": "Henüz giriş yapmadı",
                    "skor": 0, 
                    "seviye": 1
                }
                veri_yaz(veri)
                mesaj = f"'{k_adi}' başarıyla kaydedildi!"
        elif islem == "giris":
            if k_adi in veri and veri[k_adi]["sifre"] == sifre:
                veri[k_adi]["son_giris"] = zaman
                veri_yaz(veri)
                mesaj = f"Hoş geldin, {k_adi}! Giriş başarılı."
            else:
                mesaj = "Hatalı kullanıcı adı veya şifre!"
                
    return render_template_string(HTML_SAYFA, mesaj=mesaj)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
