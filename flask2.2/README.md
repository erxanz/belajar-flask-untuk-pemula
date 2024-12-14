### Template dengan Jinja2
#### Apa itu Jinja2?
Jinja2 adalah engine template yang digunakan Flask untuk memisahkan logika aplikasi dengan tampilan HTML. Anda bisa memasukkan data Python ke dalam HTML menggunakan sintaks Jinja2.

---

### Static Files
#### Apa itu Static Files?
Static files adalah file yang tidak berubah selama runtime aplikasi, seperti CSS, JavaScript, atau gambar.

---

#### Struktur Folder:
```
my_flask_app/
│
├── app.py
├── static/
│   ├── css/styles.css
│   └── img/logo.png
└── templates/
    ├── base.html
    ├── home.html
    └── profile.html
```

---

#### Kode Contoh dengan Template:

**File `app.py`:**
```python
from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def home():
    return render_template('home.html', title='Home Page', content='Welcome to the home page of the Flask app!')

# Define the route for the profile URL
@app.route('/profile')
def profile():
    user = {
        "name": "Erxanz",
        "age": 20,
        "hobby": "coding",
    }
    return render_template('profile.html', title='Profile Page', user=user)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
```

**File `templates/base.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>{{ title }}</title>
</head>
<body>
    <header>
        <img src="{{ url_for('static', filename='img/kopi.png') }}" alt="kopi" width="50" height="50">
        <nav>
            <a href="/">Home</a> | <a href="/profile">Profile</a>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

**File `templates/home.html`:**
```html
{%  extends 'base.html' %}

{%  block content %}
    <h1>Welcome to Flask</h1>
    <p>Halaman home</p>
    <p>{{ content }}</p>
{% endblock %}
```

**File `templates/profile.html`:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Profile Page</h1>
    <ul>
        <li>Nama : {{ user.name }}</li>
        <li>Umur : {{ user.age }}</li>
        <li>Hobi : {{ user.hobby }}</li>
    </ul>
{% endblock %}
```

---

#### Penjelasan:

**Inheritance template:**
- `base.html` adalah template dasar dengan struktur HTML umum.
- File `home.html` dan `profile.html` memperluas (`extends`) `base.html`.

**Sintaks Jinja2:**
- `{{ title }}`: Menampilkan variabel Python.
- `{% block content %}{% endblock %}`: Membuat bagian konten yang bisa diisi oleh template child.

**Dynamic data:**
- Variabel `user` di `app.py` dikirim ke template `profile.html` untuk ditampilkan.

---

#### Kode untuk Static Files:

**File `static/styles.css`:**
```css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f0f0f0;
    color: #333;
}

header nav a {
    margin: 0 10px;
    text-decoration: none;
    color: #007BFF;
}

header nav a:hover {
    text-decoration: underline;
}
```

**Ubah File `templates/base.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a> | <a href="/profile">Profile</a>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

---

#### Menampilkan Gambar (Opsional):
Tambahkan file gambar `kopi.png` ke folder `static/` dan tambahkan di `base.html`:

```html
<header>
    <img src="{{ url_for('static', filename='img/logo.png') }}" alt="Logo" width="50" height="50">
    <nav>
        <a href="/">Home</a> | <a href="/profile">Profile</a>
    </nav>
</header>
```



