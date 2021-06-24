from flask import Flask, render_template
from threading import Thread
app = Flask('app')

@app.route("/delete")
def delete():
  return render_template("Delete.html")


@app.route('/')
def hello_world():
  return "hello"

@app.route('/add')
def adding():
  return "adding interface"

def host():
  app.run(host='0.0.0.0', port=8080)

def alive():
  t = Thread(target = host).start()