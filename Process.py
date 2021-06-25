import requests, random
from replit import db
def link_filter(link):
  if "repl.co" in link:
    try:
      requests.get(link,timeout=2)
      return "good"
    except:
      return "error"
  else:
    return "error"

def check_dupes(link):
  status = "Good"
  for item in db.values():
    if item == link:
      status = "error"
  return status

def rand():
  return random.randint(10000,99999)

def generateID():
  r = rand()
  while r in db.keys():
    r = rand()
  return r

def add_db(ID,link):
  try:
    db[ID] = link
    return "added"
  except Exception as e:
    return e