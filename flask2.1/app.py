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
@app.route('/user/<string:username>')
def user(username):
    return f"<h1>User Page</h1><br><p>Welcome, {username}!</p>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)