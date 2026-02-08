#display art
from art import logo,vs
from game_data import data
import random

def format_data(account):
    """takes the account data and returns the format the acc data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_desc},from {account_country}."

def check_answer(user_guess, a_follower,b_follower ):
    """takes the user's guess and the followers count and return if they got it right"""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #generate a random acc from game data
    #make the account position B become the acc at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #ask user for guess
    guess = input("who has more followers? 'A' or 'B': ").lower()

    print("\n"*10)

    #check if the user is correct
    # - get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_account,b_follower_account)

    #get feedback
    #score keeping

    if is_correct:
        score+=1
        print(f"you're right! score:{score}")
    else:
        print(f"sorry, you're wrong! final score: {score}")
        game_should_continue = False


#make it repeatable
