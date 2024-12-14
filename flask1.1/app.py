from flask import Flask

# Inisialisasi Flask
app = Flask(__name__)

# Routing utama untuk halaman utama
@app.route('/')
def home():
    return 'Hello, World!, Uji Coba Flask Pertama'

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')