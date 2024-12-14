## Routing dan Views

### Apa itu Routing?
Routing adalah proses menghubungkan URL dengan fungsi tertentu di aplikasi Flask. Setiap route memiliki path unik yang digunakan untuk mengakses halaman tertentu.

### Kode Contoh untuk Routing

```python
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def home():
    return "<h1>Home Page</h1><br><p>Welcome to the home page of the Flask app!</p>"

# Define the route for the profile URL
@app.route('/profile')
def profile():
    return "<h1>Profile Page</h1><br><p>Welcome to the profile page of the Flask app!</p>"

# Route dengan parameter dinamis
# @app.route('/user/<username>') # cara 1
@app.route('/user/<string:username>') # cara 2
def user(username):
    return f"<h1>User Page</h1><br><p>Welcome, {username}!</p>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
```

### Penjelasan

#### Route Statis

- **`@app.route('/')`**: Menentukan path URL (`/`) untuk halaman utama.
- Fungsi `home()` merespons ketika path tersebut diakses.

#### Route dengan Parameter Dinamis

- **`@app.route('/user/<string:username>')`**: Menangkap variabel `username` dari URL.
- Anda bisa menentukan tipe parameter, misalnya `int`, `string`, atau `float`.

### Jalankan Aplikasi

1. Jalankan aplikasi:
   ```bash
   python app.py
   ```

2. Buka URL berikut:
   - **Halaman utama**: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
   - **Halaman profil**: [http://127.0.0.1:5000/profile](http://127.0.0.1:5000/profile)
   - **Halaman pengguna**: [http://127.0.0.1:5000/user/<nama>](http://127.0.0.1:5000/user/<nama>) (contoh: [http://127.0.0.1:5000/user/namaKamu](http://127.0.0.1:5000/user/namaKamu)).

---
