#Date: 3/15/2017
#Author: Naylene Rondon
#Filename: pizza_language_NayleneRondon.py
#Purpose: Practice With Dictionaries

#Start

#Variable/Dictionary
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
    "phil" : "python",
    }

for name in sorted(favorite_languages.keys()):  #Sorted Function
    print(name.title() + ", thank you for taking the poll.")

print("\n\nPopular languages in the poll : ")
for language in sorted(favorite_languages.values()):
      print(language.title())
    

#End
