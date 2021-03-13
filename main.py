import random
import time
#====================
def generate_path(size):
  """ create a path and fill with "s" """
  for item in range(size):
    path.append("s")
  #print(path)
#====================
def hide_eggs(size,number_eggs):
  """ hide eggs at random locations along the path """
  for item in range(number_eggs):
    egg_location = random.randint(0,size-1)
    #print(egg_location, end=",")
    path[egg_location] = "E"
  #print(path)
#====================
def find_eggs(size,hop):
  location = 0 #stars on 1st stone of path
  number = 0
  
  while (location + hop) <= (size-1):
    location += hop
    print("hop...", end = "")
    time.sleep(random.randint(1,3)/2)
  
    if path[location] == "E":
      number += 1
      print("\nFound a egg!")

  print(f"\nThe Easter bunny has found {number} egg(s)")
#====================
# MAIN PROGRAM
path = []
path_size = 10
number_eggs = 20

generate_path(path_size)

# random.seed(10)
hide_eggs(path_size,number_eggs)

print("<-- Easter Egg Hunt -->")
print("Welcome to the annual Easter Egg hunt!")
print(f"Your Easter Bunny will look for {number_eggs} Easter Eggs along a {path_size}m path")
print("-" * 30)
bunny_name = input("Enter a name for your Easter Bunny\n\t--> ")
print("-" * 30)

hop_size = random.randint(1,5)
print(f"{bunny_name}\'s hop size is {hop_size}")
print(f"How many eggs will {bunny_name} find along the path?\n")

find_eggs(path_size,hop_size)