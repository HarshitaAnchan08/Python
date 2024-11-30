#Word Counter Game

#Initial print statements
print("Lets play WORDS COUNTING GAME")
print("You have 5 chances")

#predefined string
string="Python is a popular programming language Python can be used on a server to create web applications."

#user have only 5 chances to win these game
chance=5

#splitting words and counting them each
words=len(string.split())

#running while loop to check if user entered the right input integer
while chance>0:
    user_inp=int(input("\nGuess the number of words in string : "))
    if(user_inp==words):
        print("Congratulations, You guessed it right...")
        break
    elif(user_inp>words):
        print("Guess a smaller number of words")
    elif(user_inp<words):
        print("Guess a larger number of words ")

    #if user enters wrong integer, then chance will be reducing by 1
    chance=chance-1

#if user uses all chances then, the user loses the game
if chance==0:
    print("Sorry, you lose the game")
    print("The correct number of words are : ",words)



