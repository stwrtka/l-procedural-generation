import turtle
import mysql.connector
from mysql.connector import errorcode

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.left(90)
turtle.speed(10)

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

#MySQL login
while True:
    username = input("Enter your MySQL username: ")
    password = input("Enter your MySQL password: ")
    database = input("Enter database: ")
    try:
        my_database = mysql.connector.connect(
            host = "",
            user = str(username),
            password= str(password),
            database=str(database)
        )
        break
    except mysql.connector.Error as err:
        print(f"{err}")

my_cursor = my_database.cursor()
query = input("Enter a query: ") #user can enter any query

while True: #runs until a vaild query
    try: 
        my_cursor.execute(query)
        break
    except mysql.connector.Error as err:
        print(f"{err}")

for x in my_cursor: #prints row results
    print(x)

#Deciding what the axiom will be by checking if the numebr of rows in they query result is even or odd
#if the query result is even axiom = FF
#if query result is odd axiom = F
if my_cursor.rowcount % 2 == 0:
    axiom = "FF"
else:
    axiom = "F"
print(axiom)

iterate(axiom, 2)

turtle.getscreen()._root.mainloop()
my_cursor.close()