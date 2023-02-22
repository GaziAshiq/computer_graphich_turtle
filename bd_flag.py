import turtle

turtle.left(90)
turtle.backward(100)
turtle.forward(250)

turtle.color('green')
turtle.begin_fill()
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()

turtle.color('green')

turtle.goto(65, 125)
turtle.color('red')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.hideturtle()

turtle.exitonclick()
