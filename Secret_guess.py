import random
secret_number = random.randint(0,10)
#print(secret_number)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit: 
   print("Quess any number between 0-10..")
   guess = int(input('guess: '))
   guess_count =  guess_count + 1 
   if guess == secret_number:
    print("congraturations")
    print("You won!")
    break
else:
  print("Sorry! You lost.")
