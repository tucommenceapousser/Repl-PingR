from flask import Flask, render_template, request, render_template_string
from threading import Thread
from Processs import check_dupes, generateID, add_db, find_ID, delete_link, link_filter
from urllib.parse import urlparse
import requests, random, time, Keepp, os
from replit import db

app = Flask('app')
link =""
def delete_link(ID):
  if ID in db:
      del db[ID]

      # Delete the corresponding ID and URL from id.txt
      with open("id.txt", "r") as id_file:
          lines = id_file.readlines()

      with open("id.txt", "w") as id_file:
          for line in lines:
              parts = line.strip().split()
              if len(parts) == 2 and parts[0] != ID:
                  id_file.write(line)

@app.route("/delete", methods=["POST", "GET"])
def delete():
  if request.method == "POST" and "LinkID" in request.form:
      global linkID
      linkID = request.form['LinkID'].strip()
      status = find_ID(linkID)
      if status == "error":
          return render_template("DeleteError.html", error="Link ID not found", title=" error")
      else:
          return render_template("DeleteConfirm.html", thelink=status)
  elif request.method == "POST" and "options" in request.form:
      if request.form["options"] == "Yes":
          delete_link(linkID)
          return render_template('DeleteError.html', error="Link successfully deleted!", title=" ")
      else:
          return render_template("DeleteError.html", error="The link wasn't deleted as you opted for it.", title=" error")
  return render_template("Delete.html")


@app.route('/')
def hello_world():
    homepage_template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Project Pinger Tool</title>
        </head>
        <body style="background-color: #f2f2f2; text-align: center; padding: 50px;">
            <h1 style="color: #4285f4;">Project Pinger Tool</h1>
            <p style="color: #555;">Keep your Replit projects awake!</p>
            <p style="color: #555;">Developed by trhacknon</p>
            <p style="color: #555;">Visit pages: <a href="/delete">/delete</a>, <a href="/add">/add</a>, and <a href="/id">/id</a></p>
        </body>
    </html>
    """
    return homepage_template

@app.route('/add', methods=['POST', 'GET'])
def adding():
    if request.method == "POST":
        links = request.form['links'].strip().split('\n')
        valid_links = []

        for link in links:
            if not link.startswith("https://"):
                link = "https://" + link

            link_status = link_filter(link)
            if link_status != "error":
                if check_dupes(link) != "error":
                    ID = generateID()
                    add = add_db(ID, link)
                    if add == "added":
                        valid_links.append({"link": link, "ID": ID})

                        # Save ID and URL to id.txt
                        with open("id.txt", "a") as id_file:
                            id_file.write(f"{ID} {link}\n")

        return render_template("Added.html", links=valid_links)

    return render_template("Add.html")

@app.route('/id')
def show_ids():
    id_list = []

    # Read contents from id.txt and store them in id_list
    with open("id.txt", "r") as id_file:
        for line in id_file:
            parts = line.strip().split()
            if len(parts) == 2:
                id_list.append({"ID": parts[0], "URL": parts[1]})

    return render_template("ShowIds.html", id_list=id_list)

def host():
  app.run(host='0.0.0.0', port=8080)

def alive():
  t = Thread(target = host).start()