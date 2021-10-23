
Pin = input("Enter any four Digits :: ")
Pin = list(Pin)
print(Pin)
import random
for i in range(50):
  random.shuffle(Pin)
  print(Pin)
# use sets to remove duplicates
