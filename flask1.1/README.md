# Dokumentasi Dasar-Dasar Flask versi 3

Selamat datang di panduan dasar Flask! Dokumentasi ini akan membantu Anda memahami langkah-langkah untuk memulai dengan Flask, termasuk membuat aplikasi "Hello World" pertama Anda. Mari kita mulai!

---

## 1. Instalasi Flask

### Persyaratan:
- Pastikan Python sudah terinstal di komputer Anda (minimal versi 3.7).

### Langkah-Langkah:

1. **Buat Virtual Environment** *(opsional, tapi direkomendasikan)*:
   ```bash
   python -m venv env
   ```

2. **Aktifkan Virtual Environment**:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

3. **Instal Flask**:
   ```bash
   pip install flask
   ```

---

## 2. Struktur Proyek Sederhana

Susun direktori proyek Anda dengan struktur berikut:

```plaintext
my_flask_app/
|
└── app.py      # File utama aplikasi Flask
```

---

## 3. Membuat Aplikasi Flask Pertama

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
    app.run(debug=True)
```

### Penjelasan Kode:

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
   http://127.0.0.1:5000/
   ```

3. Anda akan melihat pesan berikut:
   ```plaintext
   Hello, World! Ini aplikasi Flask pertamaku!
   ```

---

### Selesai
