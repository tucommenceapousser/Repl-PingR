from flask import Flask, render_template, request
from threading import Thread
import Process
from Process import check_dupes, generateID, add_db, find_ID, delete_link
app = Flask('app')
link =""
@app.route("/delete",methods = ["POST","GET"])
def delete():
  if request.method == "POST" and "LinkID" in request.form:
    global linkID
    linkID = request.form['LinkID'].strip()
    status = find_ID(linkID)
    if status == "error":
      return render_template("DeleteError.html",error="Link ID not found",title = " error")
    else:
      return render_template("DeleteConfirm.html", thelink = status)
  elif request.method == "POST" and "options" in request.form:
    if request.form["options"] == "Yes":
      delete_link(linkID)
      return render_template('DeleteError.html',error="Link successfully deleted!",title=" ")
    else:
      return render_template("DeleteError.html",error="The link wasn't deleted as you opted for it.",title=" error")
  return render_template("Delete.html")


@app.route('/')
def hello_world():
  return "Ping here."

@app.route('/add',methods = ['POST','GET'])
def adding():
  if request.method == "POST":
    link = request.form['link'].strip()
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