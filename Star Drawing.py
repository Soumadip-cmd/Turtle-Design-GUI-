import turtle
t=turtle.Turtle()
t.hideturtle()
t.screen.bgcolor("brown")
t.color("yellow")
t.shape("circle")
t.shapesize(0)
t.pensize(5)

t.up()
t.left(180)
t.fd(50)
t.begin_fill()
t.fillcolor("orange")
t.goto(-100,-100)
t.down()
t.goto(0,100)
t.goto(100,-100)
t.goto(-110,40)
t.goto(110,40)
t.goto(-100,-100)
t.end_fill()

t.up()
t.home()
t.goto(0,-23)
t.down()
t.color("yellow")
t.pensize(2)
t.begin_fill()
t.fillcolor("brown")

t.circle(30)
t.end_fill()