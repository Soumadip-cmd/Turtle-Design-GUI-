import turtle
t=turtle.Turtle()
t.screen.bgcolor("cyan")
t.shape("arrow")
t.color("#7B30BD")

t.speed(20)


for i in range(100):
    t.circle(2*i,90)
    t.left(90)
    t.circle(2*i,90)
t.up()