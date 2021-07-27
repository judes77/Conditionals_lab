print('Flip the light switch')
switch = input("Did the lamp turn on? ")
if switch == "yes":
     print("Let there be light!")
if switch == "no":
     spare_lightbulb = input("Do you have a spare lightbulb? ")
if spare_lightbulb == "yes":
     print("Change the lightbulb and turn on lamp")
else:    
    print("Go shopping and get a new lightbulb")