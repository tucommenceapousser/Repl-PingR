import requests, time, Keep
from replit import db
#NEED TO MAKE THIS A HTML INTERFACE
def ping():
  while True:
    requests.get("https://Pinger-testing.quantumcodes.repl.co/")
    time.sleep(1)  

if input("Are you the creator? Y/N (if yes, will start pinging).").upper().strip() == "Y":
  if input("Password?:  ") == os.environ['pass']:
    print("Running...")
    Keep.alive()
    ping()
  else:
    print("bruh")
else:
  if input("You want to delete your link from pinging or add a new link to ping? (Delete/Add)").strip().lower() == "delete":
    print("DELETING.. ")
    user = input("Link ID:  ")
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
    #PUT ADDING CODE HERE
  
