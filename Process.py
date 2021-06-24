import requests
def link_filter(link):
  if "repl.co" in link:
    try:
      requests.get(link,timeout=2)
      return "good"
    except:
      return "error"
  else:
    return "error"