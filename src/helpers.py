import re

def serverlist(servers):
  serverNames = []
  for server in servers:
    serverNames.append((re.search("(?<=name=').*?(?=')", server)).group())
  return(', '.join(serverNames))