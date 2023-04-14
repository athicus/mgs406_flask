from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_world():
	return	'Hello	World!'

@app.route('/python/')
def hello_python():
	return	'Hello	Python'

if __name__ == "__main__":
	app.run()
