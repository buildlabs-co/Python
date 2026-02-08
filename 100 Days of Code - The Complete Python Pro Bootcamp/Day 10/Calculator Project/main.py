from itertools import accumulate
import art
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2

keys={"+":add,"-":sub,"*":multiply,"/":divide,}

def calculator():
    print(art.logo)
    should_accumulate=True
    num1=float(input("whats the first number:"))
    while should_accumulate:
        for symbols in keys:
            print(symbols)
        operation=input("select a symbol:")
        num2=float(input("what is the next number:"))
        ans=keys[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {ans}")


        choice=input(f"type 'y' to continue calculating with {ans}or type 'n' to start fresh")
        if choice=="y":
            num1=ans
        else:
            should_accumulate=False
            calculator()
calculator()




