import requests, time, Keep, os, random
from replit import db
#NEED TO MAKE THIS A HTML INTERFACE
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
else:
  os.system('clear')
  if input("You want to delete your link from pinging or add a new link to ping? (Delete/Add)\n").strip().lower() == "delete":
    print("DELETING.. ")
    user = input("Link ID:  ").strip()
    if user in db.keys():
      print(db[user])
      if input("Is this your link?(Y/N)").upper().strip() == "Y":
        print("ohh")
        del db[user]
        print("Deleted successfully")
      else:
        print("please retry again then")
    else:
      print("not found")
  else:
    print("ADDING...")
    link = input("Url to ping?(only replit url allowed):  \n").strip()
    if ".repl.co" in link:
      print("Accepted. checking if link is real.")
      if not "https://" in link:
        link = "https://" + link
      try:
        r = requests.get(link,timeout = 3)
        print("link verification successful!")
      except:
        print("sorry. seems like the link either doesn't exist, there is a typo in link,there is no html page of the repl or you haven't run the repl.")
        exit()
      for item in db.values():
        if item == link:
          print("seems like your link is already added")
          exit()
      print("creating link ID...")
      ID = str(random.randint(10000,99999))
      while ID in db.keys():
        ID = str(random.randint(10000,99999))
      db[ID] = link
      print(f"Added {link} successfully!\n")
      print(f"Youe link ID is: {ID} . Keep this safe as it will allow you to remove the link from the pinger if you need.")
    else:
      print("Sorry. only links with .repl.co allowed")