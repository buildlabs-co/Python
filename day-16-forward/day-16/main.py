# #How to construct a new object
#
# from turtle import Turtle,Screen
# #newobject
# timmy = Turtle()
# print(timmy)
# #methods .shape()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# #attributes .canvheight
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["pikachu","lizad","chekondor","humangasor","bob"])
table.add_column("type",["electric","fire","grass","fire","rock"])
table.align = "r"
print(table)