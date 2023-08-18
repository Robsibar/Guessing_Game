import random

import sys

 

#The game ends when a player reaches 1,000 points, meaning that they need to get it on the first try. Players can also exit the game.

 

def start_game():

    highest_score = 0

    winner = " "

    next_player = "y"

    #Because the game ends at 1,000 points (first try), it continues looping until this happens

    while highest_score != 1000:

        print("Welcome to the Guessing Game!")

        print("The high score is {}.".format(highest_score))

        name = input("What is your name? ")

        #The game consits of guessing a random number between 1 and 10

        correct_number = random.randint(1,10)

        attempts = 0

        try:

            number = int(input("Please pick a number from 1 to 10, {}: ".format(name)))

        except ValueError:

            print("Oops, we only accept integers! Please try again!")

        else:

            while number != correct_number:

                #if the number is higher or lower than the range, they'll get an error message but their attempt won't count

                if number >10 or number <1:

                    print("The number has to be between 1 and 10!")       

                #if the number is incorrect, it'll say if it is higher/lower and the attempt will count

                elif number > correct_number and number <= 10:

                    print("It is lower, {}".format(name))

                    attempts += 1

                    print("Number of attempts: {}".format(attempts))

                elif number < correct_number and number >= 1:

                    print("It is higher, {}".format(name))

                    attempts += 1

                    print("Number of attempts: {}".format(attempts))

                #Here, we ask the person to try again. Nonetheless, if they don't put an integer, they'll get a value error

                try:

                    number = int(input("Please try again:  "))

                except ValueError:

                    print("Oops, we only accept integers! Please try again!")

            #When they guess, they get the following message, points, and what is the high score, and from whom. This only happens for those that do not reach the high score of 1,000 (first try)

            print("You guessed correctly!")

            score = 1000 - (attempts * 100)

            print("Your score is {}.".format(score))

            if score == 1000:

                print("It took you ONE try. Your score is {}.".format(score))

                print("We have an ULTIMATE WINNER.... Congrats, {}!!!!!".format(name))

                sys.exit("GAME OVER") 

            elif score > highest_score:

                highest_score = score

                winner = name

                print("{}, you are the new highest score. Congratulations!".format(name))          

            elif score == highest_score:

                print("It's a tie!")   

                winner = "'The Tie'"

            elif score < highest_score:

                print("The highest score is {}, {} is currently winning".format(highest_score,winner))

            print("Thanks for participating, {}!".format(name))

                #Here we are asking if there is a next player. They have to answer with Y/N, otherwise, they'll be getting an error and asked if they want to continue playing

            next_player = input("Is there a next player? (Y/N)  ")

            while next_player.lower() != "y":

                #If they decide that there is no next player, they'll get the high score and winner.

                if next_player.lower() == "n":

                    sys.exit("Okay, the winner is {} with a score of {}!\nSee you next time!".format(winner,highest_score))

                else:

                    next_player = input("Sorry, I do not understand. \nWould you like to continue playing? (Y/N)   ")       

 

 

start_game()