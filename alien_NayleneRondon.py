#Date: 3/13/2017
#Author: Naylene Rondon
#Filename: alien_NayleneRondon.py
#Purpose: Practice With Dictionaries

#Start

#Displaying Values
alien_0 = {"Color": "Green", "Points": 5}
print(alien_0["Color"]) 
print(alien_0["Points"])

new_points = alien_0["Points"]
print("Congrats! You just earned " + str(new_points) + " points!")

#Add new Key-Values
alien_0["X-Position"] = 0
alien_0["Y-Position"] = 25
print(alien_0)

#End
