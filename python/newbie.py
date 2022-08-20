print("Hello World")
print("I am new here")
print(5*6)
print("Boom Boom Boom")



import turtle
my_turtle = turtle.Turtle()

def theturtle(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

for i in range(30):
    theturtle(100,90)
    my_turtle.right(10)

