from flask import Flask, render_template, request
from threading import Thread
app = Flask('app')

@app.route("/delete",methods = ["POST","GET"])
def delete():
  if request.method == "POST":
    link = request.form['LinkID']
    print(link)
  elif "LinkID" in request.args:
    print(request.args['LinkID'])
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