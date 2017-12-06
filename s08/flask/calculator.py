from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, Ohad!</h1>'

@app.route('/pets')
def my_favorite_pet():
    return 'My favorite pet is Cat!'

@app.route('/food')
def my_favorite_food():
    return 'My favorite food is falafel!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return username

@app.route('/test/<a>/<b>')
def test(a, b):
    # show the user profile for that user
    result = a+b
    return str(result)

@app.route('/calculator/<num1>/<num2>/<operation>')
def calculate(num1, num2, operation):
    num1 = int(num1)
    num2 = int(num2)
    result = 'unknown'
    if operation=='+':
    	result = num1+num2
    elif operation=='-':
    	result = num1 - num2
    elif operation=='*':
    	result = num1 * num2
    elif operation==':':
    	result = num1 / num2
    	
    return str(result)

