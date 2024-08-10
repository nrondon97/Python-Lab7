#Date: 3/15/2017
#Author: Naylene Rondon
#Filename: favorite_langauges_NayleneRondon.py
#Purpose: Practice With Dictionaries

#Start
#Variable/Dictionary
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
    "phil" : "python",
    }

#Output
print("Sarah's favorite language is " +
      favorite_languages["sarah"].title() +
      ".")
print()

#Loop through dicitionary
for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is " +
      language.title() +
      ".")
print()

#Loop only through keys
for name in favorite_languages.keys():
    print(name.title() + ", thanks for contributing to the poll.")

print()


#Nested if in loop
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("    Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print()    


#Loop only through values
print("The following language where mentioned in the poll:")
for language in favorite_languages.values():
    print(language.title())

print()


#NEED FOR PROJECT 4
import random
word = random.choice(list(favorite_languages.keys()))
print(word)

#End
