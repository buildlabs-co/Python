import random
from art import logo
def deal_card():
    """returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """calculate scores"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score ==0 :
        return "lose, computer has blackjack"
    elif u_score ==0:
        return "you win with blackjack"
    elif u_score > 21:
        return "you went over you lose"
    elif c_score > 21:
        return "opponent went over you win"
    elif u_score >c_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score=-1
    user_score=-1
    game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your card:{user_cards},your score: {user_score}")
        print(f"computer's card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            choice= input(" another card type 'y', to pass type 'n': ")
            if choice=="y":
                user_cards.append(deal_card())
            else:
                game_over=True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(f"your final card {user_cards},your final score:{user_score} ")
    print(f"computers final card {computer_cards}, computer score:{computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play blackjack: 'y' or 'n'")=="y":
    print("\n"*10)
    play_game()