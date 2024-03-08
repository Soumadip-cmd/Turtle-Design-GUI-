import turtle
t=turtle.Turtle()
t.screen.bgcolor("black")
t.shape("arrow")
t.up()
t.goto(-190,0)

t.down()
t.speed(7)
t.color("#FD8104")
t.begin_fill()
t.fillcolor("#F5FD04")
for i in range(200):
    t.fd(400)
    t.left(170)
t.end_fill()



