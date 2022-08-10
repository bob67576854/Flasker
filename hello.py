from flask import Flask, render_template


# Create a flask
app = Flask(__name__)

# Create a route
@app.route('/')

#def index():
	#return "<h1>Hello World!</h1>"

def index():
	first_name = "John"
	stuff = "This is bold text"

	favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
	return render_template("index.html", 
		first_name=first_name,
		stuff=stuff,
		favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)

# Create custom error

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500