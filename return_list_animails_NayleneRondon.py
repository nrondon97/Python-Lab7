#Date: 3/13/2017
#Author: Naylene Rondon
#Filename: return_list_animails_NayleneRondon.py
#Purpose: Practice With Dictionaries
import random

#Start

def main():
    wordList = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

    word = YourGuess()
    print("You guessed: " + word)
    result = getRandomWord(wordList)

    if result.lower() == word.lower():
        print("Congrats")
    else:
        print("The right answer was " + result.title() + ".")
        print("Too Bad.")
    

def YourGuess():
    guess = input("Enter an animal name: ")
    return guess

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def intro():
    print("In this program, you'll try to guess what animal the computer is thinking of.")
    print("If you guess right, you win.")
    print()

    
intro()
main()

#End
