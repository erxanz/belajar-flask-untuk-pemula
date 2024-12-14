# Dokumentasi Dasar-Dasar Flask versi^3 Part-1

---

## 1. Struktur Proyek Sederhana

Susun direktori proyek Anda dengan struktur berikut:

```plaintext
my_flask_app/
|
└── app.py      # File utama aplikasi Flask
```

---

## 2. Membuat Aplikasi Flask Pertama

### Kode di `app.py`:

```python
from flask import Flask  # Import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Routing utama untuk halaman utama
@app.route('/')
def home():
    return "Hello, World! Ini aplikasi Flask pertamaku!"

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
```

### 3. Penjelasan Kode:

1. **`from flask import Flask`**
   - Mengimpor kelas Flask untuk digunakan membuat aplikasi web.

2. **`app = Flask(__name__)`**
   - Membuat instance aplikasi Flask. Parameter `__name__` digunakan untuk memberi tahu Flask lokasi file aplikasi.

3. **`@app.route('/')`**
   - Mendefinisikan route. Route adalah URL yang ditangani oleh aplikasi Flask. `'/'` adalah root URL (beranda aplikasi).

4. **`def home()`**
   - Fungsi Python yang dipanggil saat URL root diakses. Fungsi ini dikenal sebagai "view function".

5. **`return "Hello, World!"`**
   - String ini akan ditampilkan di browser ketika route `'/'` diakses.

6. **`if __name__ == '__main__'`**
   - Memastikan aplikasi hanya berjalan jika file ini dieksekusi langsung, bukan diimpor sebagai modul.

7. **`app.run(debug=True)`**
   - Menjalankan server Flask di mode debug. Mode debug memunculkan log kesalahan di terminal dan secara otomatis me-restart server jika ada perubahan kode.

---

## 4. Menjalankan Aplikasi

1. Jalankan aplikasi Flask:
   ```bash
   python app.py
   ```

2. Buka browser dan akses URL berikut:
   ```
   http://127.0.0.1:8000/
   ```

3. Anda akan melihat pesan berikut:
   ```plaintext
   Hello, World!, Uji Coba Flask Pertama
   ```

---
