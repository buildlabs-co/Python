print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("what is your age?"))
    if age>18:
        bill=20
        print("your fare is 20$")
    else:
        bill=2
        print("your fare is 2$")
    photo=input("do you want photo yes or no?")
    if photo=="yes":
        bill+=3
    print(f"your total bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
