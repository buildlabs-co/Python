try:
    age = int(input("How old are you?"))
except TypeError:
    print("type a numerical please")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
