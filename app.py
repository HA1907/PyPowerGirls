import os

from flask import Flask, render_template

app = Flask("demoApp")

@app.route("/")
def say_hello():
	return "lol"

@app.route("/<name>")
def say_hello_with_name(name):
	return "Hello {}".format (name)

@app.route("/hello/<name>")
def say_hello_the_old_way_with_name(name):
	return render_template ("index.html", name=name)	

If 'PORT' in os.environ:
	app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
	app.run(debug=True)
