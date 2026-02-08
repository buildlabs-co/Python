# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
def highest_bidder(dic):
    winner=""
    amt=0
    for bidder in dic:
        bid_amount=dic[bidder]
        if bid_amount>amt:
            amt=bid_amount
            winner=bidder
    print(f"the winner is :{winner}")

bids={}
bidding=True
print("welcome to blind bid!")
while bidding:
    name = input("what is your name?: ")
    bid = int(input("what is your bid:$ "))
    bids[name] = bid
    ask = input("are there any other bidder? type 'yes' or 'no'\n").lower()
    if ask=="yes":
        print("\n"*8)
    elif ask=="no":
        bidding=False
        highest_bidder(bids)


    # TODO-4: Compare bids in dictionary





