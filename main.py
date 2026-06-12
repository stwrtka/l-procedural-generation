import turtle

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.speed(100)

axiom = "FF"
angle = 90
len = 3

#rules
#F = 
#- =
#+ =
#L
#[ = start branch
#] = end branch

def replace_variable(variable):
    if variable == 'F':
        return 'F-F+F+F-F'
    elif variable == 'L':
        return 'L-F'
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
        else:
            continue

def iterate(string, count):
    if count == 0:
        return
    else:
        draw(string)
        string = expand_string(string)
        iterate(string, count)  

iterate(axiom, 2)
turtle.getscreen()._root.mainloop()