import requests, time, Keep, os, random
from replit import db
#ADD IF LOOP IN ERROR DELETE PAGE. WHEN LINK DELETED, SHOW IMAGE
Server = 1
os.system('clear')
def ping():
  while True:
    error = {}
    for ID, item in db.items():
      try:
        r = requests.get(item,timeout=2)
        print(ID, item)
      except:
        print("error :(")
        if ID in error.keys():
          error[ID] = error[ID] + 1
          if error[ID] > 4:
            del db[ID]
            del error[ID]
        else:
          error[ID] = 1
    time.sleep(1)

if input("Are you the creator? Y/N (if yes, will start pinging).").upper().strip() == "Y":
  if input("Password?:  ") == os.environ['pass']:
    print("Running...")
    if Server == 1:
      Keep.alive()
      ping()
    else:
      print("server is off...")
      exit()
  else:
    print("bruh")