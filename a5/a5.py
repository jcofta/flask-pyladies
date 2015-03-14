from flask import render_template
from flask import Flask, session, request, flash, redirect, url_for, escape
import math

users = [
{
	'username' : 'user1',
	'password' : 'pass1'	
},
{
	'username' : 'admin',
	'password' : 'admin'
}
]

app = Flask(__name__)
app.secret_key = 'my_biggest_secret'

@app.route("/")
def index():
	if 'username' in session:
		return render_template("index.html", username=escape(session['username']))	
	return render_template("index.html", username=None)

@app.route("/login", methods=['GET','POST'])
def login():
	if 'username' in session:
		return redirect(url_for('index'))
	
	if request.method == 'POST':
		for user in users:
			if request.form['username'] == user['username'] and request.form['password'] == user['password']:
				session['username'] = request.form['username']
				return redirect(url_for('index'))
		flash('Wrong login or password')

	return render_template('login.html')

@app.route("/logout")
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5000)