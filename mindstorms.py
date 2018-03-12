import turtle

def draw_sqaure(some_turtle):

    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")

# create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(9)

    for i in range(1,37):
        draw_sqaure(brad)
        brad.right(10)

#create the turtle angie - Draws a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("yellow")
    #angie.circle(100)

#create the turtle bob - Draws a triangle
    #bob = turtle.Turtle()
    #bob.shape("arrow")
    #bob.color("white")
    #bob.forward(100)
    #bob.forward(100)
    #bob.left(135)
    #bob.forward(50)
    #bob.left(135)
    #bob.forward(30)

    window.exitonclick()

draw_art()