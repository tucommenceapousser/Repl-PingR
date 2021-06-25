from flask import Flask, render_template, request
from threading import Thread
import Process
from Process import check_dupes, generateID, add_db
app = Flask('app')
link =""
@app.route("/delete",methods = ["POST","GET"])
def delete():
  if request.method == "POST":
    linkID = request.form['LinkID'].strip()
    print(linkID)
  return render_template("Delete.html")


@app.route('/')
def hello_world():
  return "Ping here."

@app.route('/add',methods = ['POST','GET'])
def adding():
  if request.method == "POST":
    link = request.form['link']
    if not "https://" in link:
      link = "https://"  +  link
      link_status = Process.link_filter(link)
    print(link,link_status)
    if link_status == "error":
      return render_template("ErrorAdd.html")
    else:
      if check_dupes(link) == "error":
        return "Link already exists"
      else:
        ID = generateID()
        add = add_db(ID,link)
        if add == "added":
          return render_template("Added.html", link = link, ID = ID)
        else:
          return add
  return render_template("Add.html")

def host():
  app.run(host='0.0.0.0', port=8080)

def alive():
  t = Thread(target = host).start()