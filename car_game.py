Command = ""
started = False
while Command != "quit":
  command = input("> ").lower()
  if command == "start": 
    if started: 
      print("Car is already started! what are you doing?")
    else:
      started = True 
      print("Car has started... Get ready to GO!")
  elif command == "stop": 
    if not started: 
      print("Be careful car has already stopped")
    else:
      started = False
      print("Car has stopped...")
  elif command == "help":
    print("""
    Start... to start the car.
    stop... to stop the car
    quit... to quit the game.
    """)
  elif command == "quit": 
    break
  else:
   print("Sorry we don't understand that")
    
