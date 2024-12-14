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