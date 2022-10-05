'''this is a type of game where the comp will choose the number and the player will have to guess it, if the number entered is higher than the actual number then comp will tell to "lower your number" and vice versa....'''
import random
randnumber=random.randint(0,100)
# print(randnumber)
userguess=None
guesses=0

print("Try to find this Number X lying between 0-100")

while(userguess != randnumber):
    guesses += 1
    print(f" Guesses= {guesses}")
    userguess=int(input("Enter Your Guess: "))
    print("\n")
    if(userguess==randnumber):
        print("Congrats! You Guessed It Right :) ")

    elif(userguess>randnumber):
        print("---------Try smaller number--------- ;( \n ")
    elif(userguess<randnumber):
        print("---------Try larger number----------- ;( \n ")
    else:
        print("SORRY, Wrong Answer :(")



