import turtle
t=turtle.Turtle()
# go(x,y) function
def go(x,y):
    t.up()
    t.goto(x,y)
    t.down()

t.screen.bgcolor("black")
#box functon
def box(x,y,ang):
    go(x,y)
    t.seth(0)
    t.fd(130)
    t.seth(180+ang)
    t.fd(20)
    t.setheading(180)
    t.fd(55)
    t.up()
    t.fd(20)
    t.down()
    t.fd(55)
    t.setheading(ang)
    t.fd(20)
#singlewave Function
def singlewave():
    t.left(80)
    t.fd(20)
    t.right(150)
    t.fd(20)
    
#wave Function
def wave(a,b):
    for i in range(1,5):
        t.left(80)
        t.fd(20*(i/2))
        t.right(150)
        t.fd(20*(i/2))
        t.left(69)
    t.seth(0)
    t.fd(5)
    t.pensize(2)
    for i in range(2,5):
        t.left(80)
        t.fd((20/i)*2)
        t.right(150)
        t.fd((20/i)*2)
        t.left(69)
    singlewave()
    t.left(80)
    t.fd(10)
    t.right(150)
    t.fd(10)
    t.goto(a,b)
    t.fd(10)
   
# color of [ I ] LOVE [ U ]
t.color("white")
t.pensize(3) 

#making [ I ]..

t.speed("slow")
box(-500,-100,-90)
t.seth(90)
t.fd(20)
t.right(90)
t.fd(55)
t.left(90)
t.fd(190)
box(-500,130,90)
go(-425,110)
t.seth(270)
t.fd(190)
t.hideturtle()

#1st wave creation
t.speed("fast")
go(-300,-100)
t.showturtle()
t.seth(0)

t.fd(10)
wave(-100,-80)

#love sign

t.pensize(5)
t.seth(130)
t.fd(150)
t.speed("slowest")
t.circle(-90,200)
t.seth(70)
t.circle(-90,200)
t.fd(150)
t.pensize(2)

#second wave creation
t.seth(150)
t.fd(10)
t.speed("slow")
t.goto(100,-110)
t.speed("fast")
t.seth(0)
wave(230,-110)

#making [ U ]

go(300,130)
t.pensize(5)
t.seth(180)
t.fd(20)
t.seth(0)
t.fd(60)
t.seth(180)
t.fd(40)
t.seth(270)
t.speed("normal")
t.pensize(3)
t.fd(175)
t.seth(290)
t.circle(90,140)
t.seth(90)
t.fd(175)
t.pensize(5)
t.seth(180)
t.fd(40)
t.seth(0)
t.fd(60)
t.seth(180)
t.fd(40)
t.pensize(3)
t.seth(270)
t.fd(155)
t.right(20)
t.circle(-70,140)
t.seth(90)
t.fd(155)

t.hideturtle()

#signature
go(0,-300)
t.color("yellow")
t.write("_Soumadip Santra__",font=("Lucida Handwriting",25,"italic"),align="center",move=True)
a=input()

