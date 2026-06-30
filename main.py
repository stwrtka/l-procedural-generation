import mysql.connector
from mysql.connector import errorcode

while True: #Asking the user to login to MySQL. It will continue asking for their username and password until it's vaild
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
my_cursor.execute("SHOW DATABASES") #Showing the user all of the available databases they have in MySQL

for x in my_cursor: #Printing out the available databases to the terminal
    print(x)

while True: #Asking the user what database they want to use. It will run till a vaild database is chosen
    database = input("\nEnter database: ") 
    try: 
        my_cursor.execute("USE " + database)
        break
    except mysql.connector.Error as err:
        print(f"{err}")


while True: #Asking the user to enter a query. It will run until a vail query is entered
    query = input("Enter a query: ") 
    try: 
        my_cursor.execute(query)
        break
    except mysql.connector.Error as err:
        print(f"{err}")

#list from: https://www.w3schools.com/SQL/sql_ref_keywords.asp
#below is a list of all the keywords in MySQL
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

for x in my_cursor: #Prints out all of the row results from the query to the terminal
    print(x)

#If the number of results are even or odd will determine the intial string(axiom) used
if my_cursor.rowcount % 2 == 0: #If the number of results are even
    axiom = "FFFF" #A diffrent stirng can be used to get a different result
else: #If the number of results are odd
    axiom = "FFF" #A diffrent stirng can be used to get a different result

import turtle #Importing the turtle that will draw out the pattern. This has to be imported here so that the pop-up happens after the query result
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.speed(10)

angle = 22.5 #Angle the turtle will move when the character is '-' (left) or '+' (right) 
len = 10 #Length of the lines drawn
postions = [] #Keeps track of postion before everything inside of'[' (open branch) is drawn. So when ']' (close branch) appears the turtle can jump back to postion where ''[' open branch was called

temp_query = query.split(" ") #Spliting the query up to look at each word in the query
def create_variable_grammer(temp_query): #This function takes in the split up query and creates the defintion each variable has
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
                grammer += "F+F+F+F" #A diffrent stirng can be used to get a different result
                options += 1
            elif options == 1:
                grammer+='F-[L[LX]L+XL]+F[+FXL]-X' #A diffrent stirng can be used to get a different result
                options += 1
            else:
                grammer += 'FF+F-F+F+FF' #A diffrent stirng can be used to get a different result
                options = 0
    grammer+='F]'
    return grammer

def replace_variable(variable): #This function takes in a single character and replaces it with its respective defintion
    if variable == 'F':
        return variable_F
    else:
        return variable

def expand_string(string): #This function takes in a string and calls  replace_variable(which replaces the character with its defition) on every index
    result = ""
    for var in string:
        result += replace_variable(var)
    return result

def draw(string): #This function takes in a string and draws based on the character at that index
    for i in string:
        if i == 'F': #Forward
            turtle.forward(len)
        elif i == '-': #Left
            turtle.left(angle)
        elif i == '+': #Right
            turtle.right(angle)
        elif i == 'L': #Leaf
            turtle.showturtle()
            turtle.stamp()
        elif i == "[": #start branch
            postions.append(turtle.position())
        elif i == "]": #close branch
            if postions:
                turtle.goto(postions.pop())
        else:
            continue

def iterate(string, count): #This function will recursively call itself until the number of recursions is 0. 
    if count == 0:
        return
    else:
        #Within each call the turtle will draw out the generated string. Then call for the string to be expanded again and draw out the expanded string on the next iteration
        # print(string) #This prints out the current generated string 
        draw(string)
        string = expand_string(string)
        iterate(string, count-1)  

variable_F = create_variable_grammer(temp_query) #This is calling the function that will create defition(grammer) for a variable

iterate(axiom, 3) #starting string and number of times the rewrite should run

turtle.getscreen()._root.mainloop()
my_cursor.close()