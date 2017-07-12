from todoapp import app

@app.route('/')

def index():
	return '<h1>Hello World!</h1>'