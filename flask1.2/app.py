from flask import Flask
from datetime import datetime

# Inisialisasi Flask
app = Flask(__name__)

# Route halaman utama
@app.route('/')
def home():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"""
    <h1>Selamat Datang di Flask!</h1>
    <p>Waktu saat ini: {current_time}</p>
    <a href='/about'>Tentang Flask</a>
    """

# Route halaman tentang
@app.route('/about')
def about():
    return """
    <h1>Tentang Flask</h1>
    <p>Flask adalah web framework minimalis untuk Python.</p>
    <a href='/'>Kembali ke halaman utama</a>
    """

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True, port=8000)