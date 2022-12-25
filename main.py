import requests
import json
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
import threading
my_secret = "" # Webhook here
min_id = 5000000
max_id = 15000000
webhook = DiscordWebhook(url=my_secret)
print("Running! | Zkoo#1111")
def main():
    url = f"https://groups.roblox.com/v2/groups?groupIds={random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}%2C{random.randint(min_id,max_id)}"

    r = requests.get(url)
    try:
      r1 = json.loads(r.text)
      r1 = r1["data"]
    except:
      return
    for x in r1:
      try:
        id = x["id"]
        owner = x["owner"]
      except:
        return
   
      if owner == None:

        try:
          urlList = [f"https://groups.roblox.com/v1/groups/{id}"]
    
          t = random.choice(urlList)
          checkOwner = requests.get(t)

          checkOwner = json.loads(checkOwner.text)
          entry = checkOwner["publicEntryAllowed"]
          if entry == True:
            try:
               lock = checkOwner["isLocked"]
               f = open("lock.txt", "a+")
               f.write(f"LOCKED {id}\n")
               f.close() 
               print(f"LOCKED {id}")
            except:
              f = open("group.txt", "a+")
              f.write(f"FOUND {id}\n")
              f.close()
              info = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
              json1 = json.loads(info.text)
              name = json1["name"]
              memberCount = json1["memberCount"]
              game = requests.get(f"https://games.roblox.com/v2/groups/{id}/games?accessFilter=All&sortOrder=Asc&limit=100")
              game = json.loads(game.text)["data"]
              gameCount = len(game)
              visitGameList = []
              if gameCount == 0:
                mostVisits = "None"
              else:
                for games in game:
                    visits = games["placeVisits"]
                    visitGameList.append(visits)
                mostVisits = max(visitGameList)
              groupLink = f"https://www.roblox.com/groups/{id}"
              clothing = str(len(requests.get(f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30").json()['data']))
              embed = DiscordEmbed(title='**New Group Found!**',
                          description=f'\n\n**Ad:**\n Made by Zkoo#1111!\n\n**Group Link:**\n {groupLink}\n\n**Group ID:**\n {id}\n\n**Group Name:**\n {name}\n\n **Group Members:**\n {memberCount}\n\n **Clothing:**\n {clothing}\n\n **Games:**\n {gameCount}\n\n **Most Visited Game:**\n {mostVisits}',
                          color=10038562)
              webhook.add_embed(embed)
              t = webhook.execute(remove_embeds=True)
             
          
        except:
          return
        
        
        
      
while True:
    threading.Thread(target=main).start()           
