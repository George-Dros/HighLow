import random
from art import logo, vs
from game_data import data
import replit

SCORE = 0 
LOSE  = False

def compare(x,y):
  global SCORE
  global LOSE
  
  if x['follower_count'] > y['follower_count'] and choice == x :
    SCORE += 1
    replit.clear() 
    print(f"You're right! Current score: {SCORE}")
    return x
    
  elif y['follower_count'] > x['follower_count'] and choice == y :
    SCORE += 1
    replit.clear() 
    print(f"You're right! Current score: {SCORE}")
    return y
    
  else:
    replit.clear() 
    print(f"Sorry that's Wrong... Final score: {SCORE}")
    LOSE = True
    
print(logo)
print(" ")


a = random.choice(data)

while LOSE == False:
  
  b = random.choice(data)
  
  while a == b:
    b = random.choice(data)
  
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
  
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if choice == "a":
    choice = a
  elif choice == "b":
    choice = b

  a = compare(a,b)
   


  



