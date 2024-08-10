#Date: 3/15/2017
#Author: Naylene Rondon
#Filename: fish_guest_NayleneRondon.py
#Purpose: Practice With Dictionaries

import random
#Start

#Variables
ocean_stuff = {
    "Fish" : ["Salmon", "Red Snapper", "Tuna", "shark"],
    "plants" : ["Sea Cucumber", "Coral", "plankton"],
    "rocks" : "white"
    }

fishtype = random.choice(ocean_stuff["Fish"])  #Choice
planttype = random.choice(ocean_stuff["plants"])  #Choice
score = 0

#Input
print("Can you guess what I'm thinking? All answers belong in the ocean.")

#Round 1
print("Round 1")
guess = input("\nTry to guess which fish I'm thinking about: ")

if fishtype.lower() == guess.lower():
    print("Congrats! It was " + fishtype.title() + ".")
    score = score + 1

else:
    print("Too bad! It was " + fishtype.title() + ".")
    

#Round 2

print("Round 2")

guess = input("\nTry to guess which plant I'm thinking about: ")

if planttype.lower() == guess.lower():
    print("Congrats! It was " + planttype.title() + ".")
    score = score + 1

else:
    print("Too bad! It was " + planttype.title() + ".")



#Output score
print("Your score is : " + str(score))

#End
