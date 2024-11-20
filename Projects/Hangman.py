#Guess the word / Hangman game

#Importing random module
import random

#List of words
words=["MERCURY","VENUS","EARTH","MARS","JUPITER","SATURN","URANUS","NEPTUNE"]

#Choosing a word randomly
word=random.choice(words)

total_chances=7
#Total dashes according to word
guessed_word="-"*len(word)

#Print statements
print("---Hangman Game---")
print("\nHint : Guess a Planet")

while total_chances!=0:
    print(guessed_word)
    
    letter=input("Guess a Letter : ").upper()
    if letter in word:
        for i in range(len(word)):
            if word[i]==letter:
                guessed_word=guessed_word[:i]+letter+guessed_word[i+1:]
               # print(guessed_word)
                
        if guessed_word==word:
            print("Congratulation you won!!!")
            break
    else:
        total_chances-=1
        print("Incorrect guess")
        print("Remaining chances are : ",total_chances)
            
else:
    print("\nGame Over")
    print("You Lose")
    print("All the chances are exchausted")
print("The correct word is : ",word)
