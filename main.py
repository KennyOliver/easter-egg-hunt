import random
import time          
from vividHues import Clr #my own module for coloured strings!
#====================
def generate_path(size):
  """ create path and fill with "s" """
  for item in range(size):
    path.append("s")
  #print(path)
#====================
def hide_eggs(size,number_eggs):
  """ hide eggs at random locations on path """
  for item in range(number_eggs):
    egg_pos = random.randint(0,size-1)
    #print(egg_pos, end=",")
    path[egg_pos] = "E"
  #print(path)
#====================
def find_eggs(size,hop):
  bunny_pos = 0 #starts on 1st stone of path
  number = 0
  
  while (bunny_pos + hop) <= (size-1):
    bunny_pos += hop
    print("hop...", end = "")
    time.sleep(random.randint(1,3)/8)
  
    if path[bunny_pos] == "E":
      number += 1
      print(Clr.LIME + "Egg found!" + Clr.RESET)
  
  print(Clr.GREEN + f"\n{bunny_name} has found {number} egg(s)!" + Clr.RESET)
#====================
# MAIN PROGRAM
path = []
path_size = 50
number_eggs = 20

generate_path(path_size)

# random.seed(10)
hide_eggs(path_size,number_eggs)

print("<-- Easter Egg Hunt -->")
print(Clr.GREEN + "Welcome to the annual Easter Egg hunt!" + Clr.RESET)
print(Clr.LIME + f"Your Easter Bunny will look for {number_eggs} Easter Eggs hidden along a {path_size}m path")

print(Clr.BLACK + "-" * 30 + Clr.RESET)
bunny_name = input(Clr.YELLOW + "Enter a name for your Easter Bunny\n\t--> " + Clr.RESET)
print(Clr.BLACK + "-" * 30 + Clr.RESET)

hop_size = random.randint(1,5)
print(Clr.YELLOW + f"{bunny_name} can hop {hop_size}m")
print(Clr.PINK + f"How many eggs will {bunny_name} find along the path?\n" + Clr.RESET)

find_eggs(path_size,hop_size)