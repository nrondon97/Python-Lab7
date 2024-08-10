#Date: 3/13/2017
#Author: Naylene Rondon
#Filename: modified_alien_NayleneRondon.py
#Purpose: Passing values to a dictionary

#Start

#Minor Test
name = ["matt", "joe", "daniel", "alicia", "sarah"]

#Actual Program
alien_0 = {}  #Empty Dictionary
alien_0["color"] = "green"
alien_0["points"] = 5
alien_0["abducted"] = name  #Part of test
print(alien_0)



#Modified
print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"

print("The alien is " + alien_0["color"] + ".")


#End
