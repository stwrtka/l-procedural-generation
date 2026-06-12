import turtle

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.speed(10)

axiom = "F+F+F+F"
angle = 90
len = 10
postions = []

#rules
#F = 
#- =
#+ =
#L
#[ = start branch
#] = end branch

def replace_variable(variable):
    if variable == 'F':
        return 'F+F-F-FF+F+F-F'
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
        elif i == "[":
            postions.append(turtle.position())
        elif i == "]":
            if postions:
                turtle.goto(postions.pop())
        else:
            continue

def iterate(string, count):
    if count == 0:
        return
    else:
        print(string)
        draw(string)
        string = expand_string(string)
        iterate(string, count-1)  

iterate(axiom, 3)
turtle.getscreen()._root.mainloop()