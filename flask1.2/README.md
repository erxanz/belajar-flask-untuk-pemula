## 1. Struktur Folder Flask

Buat struktur older yang rapi:

```plaintext
my_flask_app/
|
└── app.py      # File utama aplikasi Flask
```

---

## 2. Membuat Aplikasi Flask

### Kode Lengkap di `app.py`:

```python
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
```

---

## 3. Penjelasan Kode

### Mengimpor Modul
- **`from flask import Flask`**: Mengimpor framework Flask untuk membuat aplikasi web.
- **`from datetime import datetime`**: Mengimpor modul Python bawaan untuk mendapatkan waktu saat ini.

### Inisialisasi Aplikasi
- **`app = Flask(__name__)`**: Membuat instance aplikasi Flask untuk menjalankan server dan mendefinisikan route.

### Routing dan Fungsi

#### Home Route (`/`):
- **`@app.route('/')`**: Route untuk URL utama (root).
- **`def home()`**: Fungsi yang dipanggil saat pengguna mengakses route `/`.
- Menggunakan `f-string` untuk menyisipkan waktu saat ini ke dalam HTML.

#### About Route (`/about`):
- **`@app.route('/about')`**: Route tambahan yang memberikan informasi tentang aplikasi.

### Menjalankan Server
- **`if __name__ == '__main__':`**: Memastikan kode hanya dieksekusi saat file `app.py` dijalankan langsung.
- **`app.run(debug=True)`**: Menjalankan server Flask dengan mode debug.

---

## 4. Menjalankan Aplikasi

1. Jalankan aplikasi:
   ```bash
   python app.py
   ```

2. Anda akan melihat log server seperti ini:
   ```plaintext
   * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
   ```

3. Akses URL berikut:
   - **Halaman utama**: [http://127.0.0.1:8000/](http://127.0.0.1:5000/)
   - **Halaman tentang**: [http://127.0.0.1:8000/about](http://127.0.0.1:5000/about)

---
