# import random
# import art
#
#
# print(art.logo)
# print("Welcome to the number guessing game")
# print("I am thinking of a number between 1 and 100.")
#
# number = random.randint(1,100)
#
# difficulty= input("choose a difficulty. type 'easy' or 'hard': ").lower()
#
#
# chance=10
# if difficulty == 'easy':
#     easy=True
#     while easy:
#         print(f"you have {chance} attempts remaining to guess the number ")
#         chance-=1
#         guess=int(input("make a guess: "))
#         if guess == number:
#             print(f"You got it, the answer was {number}.")
#             easy=False
#         elif chance == 0:
#             print("You've run out of guesses. Refresh the page to run again.")
#             break
#         else:
#             if guess < number:
#                 print("Too low")
#             elif guess > number:
#                 print("Too high")
#             print("Guess again.")
#
# elif difficulty =="hard":
#     chances=5
#     hard = True
#     while hard:
#         print(f"you have {chances} attempts remaining to guess the number ")
#         chances -= 1
#         guess = int(input("make a guess: "))
#         if guess == number:
#             print(f"You got it, the answer was {number}.")
#             hard = False
#         elif chances == 0:
#             print("You've run out of guesses. Refresh the page to run again.")
#             break
#         else:
#             if guess < number:
#                 print("Too low")
#             elif guess > number:
#                 print("Too high")
#             print("Guess again.")
#
import random

EASY=10
HARD=5


def check_number(user_guess,actual_number,turns):
    if user_guess > actual_number:
        print("too high")
        return turns - 1
    elif user_guess < actual_number:
        print("too low")
        return  turns - 1
    else:
        print(f"you got it, the number was {actual_number}")

def difficulty():
    level=input("chose easy or hard: ").lower()
    if level =="easy":
        return EASY
    else:
        return HARD
def game():
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100.")
    number= random.randint(1,100)
    turns=difficulty()
    guess=0
    while guess !=number:
        print(f"you have {turns} attempts left")
        guess=int(input("guess: "))
        turns=check_number(guess, number,turns)
        if turns == 0:
            print("no more chances")
            return


game()
