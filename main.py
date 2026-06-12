import turtle

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.home()

axiom = "FF"
string = axiom
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

def expand_string(string):
    new_string = ''
    for i in string:
        new_string = new_string + replace_variable(str(i))
    return new_string

new_string = expand_string(axiom)
print(new_string)

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
turtle.getscreen()._root.mainloop()