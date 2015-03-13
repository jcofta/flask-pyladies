from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html', text='Hello, guys!')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5000)cp