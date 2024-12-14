from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('home.html')

# Route untuk halaman about
@app.route('/about')
def about():
    return render_template('about.html')

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True, port=8000)