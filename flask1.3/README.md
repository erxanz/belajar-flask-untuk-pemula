# Dokumentasi Dasar-Dasar Flask Part-3
## Menambahkan HTML dan CSS untuk Tampilan

---

### Struktur Folder

```plaintext
my_flask_app/
|
├── app.py
├── static/
│   └── styles.css
└── templates/
    └── home.html
```
### File `static/styles.css`:

```css
body {
    font-family: Arial, Helvetica, sans-serif;
    margin: 20px;
    background-color: #f9f9f9;
    color: #333;
}

h1 {
    color: #1d2d3d;
}

p {
    line-height: 1.6;
}
```

### File `templates/home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>Home | Flask</title>
</head>
<body>
    <h1>Halaman Home</h1>
    <p>Ini adalah aplikasi pertama saya</p>
    <a href="{{ url_for('about') }}">about</a>
</body>
</html>
```

### File `templates/about.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>About | Flask</title>
</head>
<body>
    <h1>Halaman About</h1>
    <p>Selamat datang di halaman about flask</p>
    <a href="{{ url_for('home') }}">home</a>
</body>
</html>
```

### Ubah Routing di `app.py`:

```python
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
```

---