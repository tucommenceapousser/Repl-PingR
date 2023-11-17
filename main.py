import requests, time, Keepp, os, random
from replit import db
#ADD IF LOOP IN ERROR DELETE PAGE. WHEN LINK DELETED, SHOW IMAGE
Server = 1
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
os.system('clear')
def ping():
  while True:
    error = {}
    timing = time.time()
    for ID, item in db.items():
      try:
        r = requests.get(item,timeout=2,headers=headers)
        print(item, r.elapsed.total_seconds())
      except:
        print("error :(")
        if ID in error.keys():
          error[ID] = error[ID] + 1
          if error[ID] > 4:
            del db[ID]
            del error[ID]
        else:
          error[ID] = 1
    timing = time.time() - timing
    print(timing)
    if 240 - timing > 0:
      time.sleep(240 - timing)

if Server == 1:
  Keepp.alive()
  ping()
else:
  print("server is off...")
  exit()