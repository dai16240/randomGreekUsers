# Import modules
from flask import Flask, render_template, jsonify
from person import *

# Create Flask Instance
app = Flask(__name__)

# Index Route
@app.route('/')
def index():
	person = generate_person()
	return render_template('index.html', person=person)

# Api Get User Route
@app.route('/api/user')
def get_user():
	person = generate_person()
	return jsonify(user=person)

# Api Get N Users Route
@app.route('/api/users/<int:n>')
def get_users(n):
	users = []
	for _ in range(n):
		person = generate_person()
		users.append(person)
	return jsonify(users=users)