import turtle

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.home()

axiom = "FF"
iterate = 3
angle = 90

#rules
#F = 
#- =
#+ =
#L
#[ = start branch
#] = end branch

def replace_variable(variable):
    if variable == 'F':
        return 'FF+F-[+-F]'
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
            turtle.forward(20)
        elif i == '-': #left
            turtle.left(angle)
        elif i == '+': #right
            turtle.right(angle)
        elif i == 'L': #leaf
            turtle.showturtle()
            turtle.stamp()
        i+= 1

def iterate(string, count):
    if count == 0:
        print(string)
        return str(string)
    else:
        count -=1
        string = expand_string(string)
        iterate(string, count)

print(iterate(axiom, 2))

#turtle.getscreen()._root.mainloop()