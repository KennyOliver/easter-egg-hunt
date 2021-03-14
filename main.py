import random
import time          
from vividHues import Clr #my own module for coloured strings!
#====================
def generate_path(length):
  """ create path and fill with "s" """
  for item in range(length):
    path.append("s")
  #print(path)
#====================
def hide_eggs(length,number_eggs):
  """ hide eggs at random locations on path """
  for item in range(number_eggs):
    egg_pos = random.randint(0,length-1)
    #print(egg_pos, end=",")
    path[egg_pos] = "E"
  #print(path)
#====================
def find_eggs(length,hop):
  bunny_pos = 0 #starts on 1st stone of path
  egg_count = 0
  
  while (bunny_pos + hop) <= (length-1):
    bunny_pos += hop
    print("hop...", end = "")
    time.sleep(random.randint(1,3)/8)
  
    if path[bunny_pos] == "E":
      egg_count += 1
      print(Clr.LIME + "Egg found!" + Clr.RESET)
  
  print(Clr.GREEN + f"\n{bunny_name} has found {egg_count} egg(s)!" + Clr.RESET)
#====================
# MAIN PROGRAM

# random.seed(10)
path = []
path_length = random.choice([25,50,75])
number_eggs = random.choice([10,15,20])

generate_path(path_length)
hide_eggs(path_length,number_eggs)
hop_size = random.randint(1,5)

print("<-- Easter Egg Hunt -->")
print(Clr.GREEN + "Welcome to the annual Easter Egg hunt!" + Clr.RESET)
print(Clr.LIME + f"Your Easter Bunny will look for {number_eggs} Easter Eggs hidden along a {path_length}m path")

print(Clr.BLACK + "-" * 30 + Clr.RESET)
bunny_name = input(Clr.YELLOW + "What will you call your Easter Bunny?\n\t--> " + Clr.RESET)
print(Clr.YELLOW + f"{bunny_name} can hop {hop_size}m!")
print(Clr.BLACK + "-" * 30 + Clr.RESET)

print(Clr.PINK + f"How many eggs will {bunny_name} find along the path?" + Clr.RESET)

find_eggs(path_length,hop_size)