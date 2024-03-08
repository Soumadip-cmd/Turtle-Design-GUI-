import turtle
t=turtle.Turtle()
#color
Blue='#7878D1'
brown='#5C3207'
red='#A10E18'
orange='#EB531B'
green='#078117'
light_blue='#372BDE'
deep_brown='#400002'
whiteS='#CAC3B4'
dark_blue='#04023D'

t.speed('normal')

t.screen.bgcolor(Blue)
t.shape("Arrow")
t.color("black")

def go(x,y):
    t.up()
    t.goto(x,y)
    t.down()

#flag moving part
def flagM(ang):
    t.seth(ang)
    t.circle(-90,100)
    t.circle(90,100)
# styl function 
def styl(x,y,rad):    
    t.begin_fill()
    t.fillcolor(red)
    go(x,y)
    t.circle(rad)
    t.end_fill()
    
# flagpart Function: 
def flagpart(x,y,ang):
    go(x,y)
    t.seth(270)
    t.fd(60)
    flagM(ang)
    t.fd(17)
    t.left(32)
    t.circle(270,9)
    t.left(140)
    t.circle(-90,100)
    t.circle(90,100)
    
    
go(-90,-250)
t.seth(90)
t.pensize(5)
t.begin_fill()
t.fillcolor(brown)
for i in range(2):
    t.fd(500)
    t.right(90)
    t.fd(15)
    t.right(90)
t.end_fill()
go(-90,250)


#peak part

styl(-90,250,-10)
go(-75,243)
t.begin_fill()
t.fillcolor("white")
#upper part:

flagM(60)
t.right(130)
t.circle(-270,42)

#lower part:

t.right(10)
t.circle(-90,100)
t.circle(90,96)

t.end_fill()
t.seth(90)
t.fd(180)
    
#upper part color: 
t.speed('slowest')
t.begin_fill()
t.fillcolor(orange)
flagpart(-75,250,60)
t.end_fill()

#lower part: 
t.speed('slow')
t.begin_fill()
t.fillcolor(green)

flagpart(-75,130,53)
t.right(20)
t.fd(12)
t.end_fill()
t.seth(90)
t.fd(135)

#curving part:
go(210,140)
t.fd(20)
t.seth(270)
t.fd(40)

#chakra making
go(65,195)
t.shape("Arrow")
t.speed("fastest")
t.color(light_blue)
t.pensize(2)
t.begin_fill()
t.fillcolor('white')
for i in range(50):
    t.fd(50)
    t.left(140)
t.end_fill()
t.color("black")
t.left(-70)
t.pensize(3)
t.circle(26)
t.hideturtle()
go(-90,-220)
t.showturtle()
t.setheading(180)

#[_____] making: 

t.speed('normal')
t.begin_fill()
t.fillcolor(deep_brown)
t.fd(250)
t.left(90)
t.fd(50)
t.left(90)
t.fd(550)
t.left(90)
t.fd(50)
t.seth(180)
t.fd(285)
t.seth(270)
t.fd(32)
t.setheading(180)
t.fd(15)
t.setheading(90)
t.fd(33)
t.end_fill()

# wishing..
t.speed('slow')
go(-60,-130)

t.color(orange)
t.write("Happy ",font=('Forte',36,'italic'),move=True)
t.color(whiteS)
t.write("Independence ",font=('Forte',36,'italic'),move=True)
t.color(green)
t.write("Day",font=('Forte',36,'italic'),move=True)
go(-40,-180)
t.color(light_blue)
t.write("🤗to all (●'◡'●)",font=('Forte',36,'italic'),move=True)

#signature Making...
t.speed('slow')
t.hideturtle()
go(-90,-340)
t.color(dark_blue)
t.write("_Soumadip Santra__",font=("Lucida Handwriting",25,"italic"),align="center",move=True)

