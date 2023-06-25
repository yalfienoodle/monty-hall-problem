import random
def choosing():
  open("wl.txt","w")
  while True:
    doors = []
    available = ["0","1","2"]
    for _ in range(3):
      choice = random.choice(available)
      doors.append(choice)
      available.remove(choice)
    choice = random.randint(0,2)
    doos = ""
    for item in doors:
      doos += f"{item} "
    open("choose.txt","w").write(doos)
    choose = open("choose.txt","r").read().split(" ")
    choose.remove(choose[-1])
    choose.remove(doors[choice])
    while True:
      try:
        choose.remove(f"{random.randint(1,2)}")
        break
      except:
        continue
    if random.choice(choose) == "0":
      open("wl.txt","a").write("w")
      print("WIN")
    else:
      open("wl.txt","a").write("l")
      print("LOSS")
def dataCounting():
  data = open("wl.txt","r").read()
  wins = data.count("w")
  losses = data.count("l")
  total = wins+losses
  print("When swapping")
  print(f"   Wins: {wins}/{total} ({int(round(wins/total,2)*100)}% win rate)")
  print(f"   Losses: {losses}/{total} ({int(round(losses/total,2)*100)}% loss rate)")
if input("1 for the problem 2 for the data counting >> ") == "1":
  choosing()
else:
  dataCounting()
