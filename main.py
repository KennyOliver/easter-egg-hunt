import random
import time
#====================
def fill_path(size):
  """ create a path and fill with "s" """
  for item in range(size):
    path.append("s")
  print(path)
#====================
def hide_eggs(size,number_eggs):
  """ hide eggs at random locations along the path """
  for item in range(number_eggs):
    egg_location = random.randint(0,size-1)
    print(egg_location)
    path[egg_location] = "E"
  print(path)
#====================
def bunny_hops(size,hop):
  location = 0 #stars on 1st stone of path
  number = 0
  
  while (location + hop) <= (size-1):
    location += hop
    print("hop...", end = "")
    time.sleep(1)
  
    if path[location] == "E":
      number += 1
      print("\nFound a egg!")

  print(f"\nThe Easter bunny has found {number} egg(s)")
#====================
# MAIN PROGRAM
print("Welcome to the Easter Egg hunt")
path = []
path_size = 10

fill_path(path_size)

# random.seed(10)
number_eggs = 5
hide_eggs(path_size,number_eggs)

hop_size = random.randint(1,3)
print(f"The Easter bunny\'s hop size is {hop_size}")
print("How many eggs can your bunny find along the path?\n")

bunny_hops(path_size,hop_size)