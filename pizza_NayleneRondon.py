#Date: 3/15/2017
#Author: Naylene Rondon
#Filename: pizza_NayleneRondon.py
#Purpose: Practice With Dictionaries

#Start
pizza = {
    "crust" : "thick",
    "toppings" : ["mushrooms", "extra cheese", "pepperoni"]
    }
    
print("You ordered a " + pizza["crust"] + "-crust pizza " +
      "with the following toppings: ")

for topping in pizza["toppings"]:
    print("\t" + topping)

#End
