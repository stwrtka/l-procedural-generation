import mysql.connector
from mysql.connector import errorcode
#MySQL login
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
    except mysql.connector.Error as err:
        print(f"{err}")

my_cursor = my_database.cursor()
my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
    print(x)

database = input("\nEnter database: ")
while True: #runs until a vaild query
    try: 
        my_cursor.execute("USE " + database)
        break
    except mysql.connector.Error as err:
        print(f"{err}")


query = input("Enter a query: ") #user can enter any query
while True: #runs until a vaild query
    try: 
        my_cursor.execute(query)
        break
    except mysql.connector.Error as err:
        print(f"{err}")

#list from: https://www.w3schools.com/SQL/sql_ref_keywords.asp
key_words = ["ADD", "ADD CONSTRAINT", "ALL", "ALTER", "ALTER COLUMN", "AND", "ANY","AS", "ASC", 
             "BACKUP DATABASE", "BETWEEN", "CASE", "CHECK", "COLUMN", "CONSTRAINT", "CREATE", 
             "CREATE DATABASE", "CREATE INDEX", "CREATE OR REPLACE VIEW", "CREATE TABLE", 
             "CREATE PROCEDURE", "CREATE UNIQUE INDEX", "CREATE VIEW", "DATABASE", "DEFAULT", 
             "DELETE", "DESC", "DISTINCT", "DROP", "DROP COLUMN", "DROP CONSTRAINT", "DROP DATABASE", 
             "DROP DEFAULT", "DROP INDEX", "DROP TABLE", "DROP VIEW", "EXEC", "EXISTS", "FOREIGN KEY", 
             "FROM", "FULL OUTER JOIN", "GROUP BY", "HAVING", "IN", "INDEX",  "INNER JOIN", "INSERT INTO",
             "INSERT INTO SELECT", "IS NULL", "IS NOT NULL", "JOIN", "LEFT JOIN", "LIKE", "LIMIT", "NOT",
             "NOT NULL", "OR", "ORDER BY", "OUTER JOIN", "PRIMARY KEY", "RIGHT JOIN", "ROWNUM", "SELECT", 
             "SELECT DISTINCT", "SELECT INTO", "SELECT TOP", "SET", "TABLE", "TOP", "TRUNCATE TABLE", 
             "UNION", "UNION ALL", "UNIQUE", "UPDATE", "VALUES", "VIEW", "WHERE"]

for x in my_cursor: #prints row results
    print(x)

#deciding what the axiom will be by checking if the numebr of rows in they query result is even or odd
if my_cursor.rowcount % 2 == 0:
    axiom = "FFFF" #if the query result is even
else:
    axiom = "FFF" #if query result is odd axiom = F

import turtle #have to import after so the turtle will draw after the query result
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.speed(10)

angle = 22.5 #angle the turtle will move when the character is -(left) or + (right) 
len = 10 #length of the lines drawn
postions = [] #keeps track of postion before [ is drawn so when ] appears the turtle can jump back to that postion

temp_query = query.split(" ")
def create_variable_grammer(temp_query):
    grammer =""
    open = 0
    options = 0
    for x in temp_query:
        if x  in key_words: 
            if open  == 0:
                grammer+= '['
                open = 1
            else:
                grammer +=']'
                open = 0
        else:
            if options == 0:
                grammer += "F+F+F+F"
                options += 1
            elif options == 1:
                grammer+='F-[[X]+X]+F[+FX]-X'
                options += 1
            else:
                grammer += 'FF+F-F+F+FF'
                options = 0
    grammer+='F]'
    return grammer

def replace_variable(variable): #this function takes in a single character and replaces it with a string
    if variable == 'F':
        return variable_F
    else:
        return variable

def expand_string(string): #this function takes in a string and calls replace_variable on every index
    result = ""
    for var in string:
        result += replace_variable(var)
    return result

def draw(string): #this function takes in a string and draws based on the character at that index
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

def iterate(string, count): #this function calls the core functions (draw and expand_string) recursively for count times
    if count == 0:
        return
    else:
        print(string)
        draw(string)
        string = expand_string(string)
        iterate(string, count-1)  

variable_F = create_variable_grammer(temp_query)

iterate(axiom, 3)

turtle.getscreen()._root.mainloop()
my_cursor.close()