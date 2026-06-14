import turtle
import mysql.connector
from mysql.connector import errorcode
while True:
    username = input("Enter your MySQL username: ")
    password = input("Enter your MySQL password: ")

    try:
        my_database = mysql.connector.connect(
            host = "",
            user = str(username),
            password= str(password)
        )
        break
    except mysql.connector.Error as error:
        print(f"{error}")
    finally:
        print("Try again")

my_cursor = my_database.cursor()
my_cursor.execute("SHOW DATABASES")

for i in my_cursor:
    print(i)

my_database.close()

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.left(90)
turtle.speed(10)

axiom = "F+F+F+F"
angle = 90
len = 25
postions = []


def replace_variable(variable):
    if variable == 'F':
        return 'FF+F-F+F+FF'
    else:
        return variable

def expand_string(string):
    result = ""
    for var in string:
        result += replace_variable(var)
    return result

def draw(string):
    for i in string:
        if i == 'F': #forward
            turtle.forward(len)
        elif i == '-': #left
            turtle.left(angle)
        elif i == '+': #right
            turtle.right(angle)
        elif i == 'L': #leaf
            turtle.showturtle()
            turtle.stamp()
        elif i == "[": #start branch
            postions.append(turtle.position())
        elif i == "]": #close branch
            if postions:
                turtle.goto(postions.pop())
        else:
            continue

def iterate(string, count):
    if count == 0:
        return
    else:
        draw(string)
        string = expand_string(string)
        iterate(string, count-1)  

iterate(axiom, 2)
turtle.getscreen()._root.mainloop()
my_cursor.close()