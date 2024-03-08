import turtle
t=turtle.Turtle()

def go(x,y):
    t.up()
    t.goto(x,y)
    t.down()

t.screen.bgcolor('black')
t.color('Red')
t.speed('slow')
t.pensize(5)

# making H leftside :
def H(x,y,ang):
    go(x,y)
    t.seth(270)
    t.fd(100)
    t.right(90+ang)
    t.fd(10)
    t.left(180)
    t.fd(40)
    t.left(180)
    t.fd(10)
    t.right(90+ang)
    t.fd(40)
    t.up()
    t.fd(20)
    t.down()
    t.fd(40)
    t.right(90+ang)
    t.fd(10)
    t.left(180)
    t.fd(40)

def call_H(x,y):
    H(x,y,0)
    go(x+20,y-40)  
    t.seth(0)
    t.fd(50)
    go(x+20,y-60)
    t.seth(0)
    t.fd(50)
    H(x+90,y,180)
      
#A left side:

def A(x,y,ang1):
    go(x,y)
    t.right(120)
    t.fd(115)
    t.right(60+(4*ang1))
    t.fd(10)
    t.right(180)
    t.fd(40)
    t.left(180)
    t.fd(10)
    t.right(120+(2*ang1))
    t.fd(37.5)
    t.up()
    t.fd(20)
    t.down()
    t.fd(35)
    

#making A:

def call_A(x,y):
    A(x,y,0)
    A(x+40,y,60)
    t.seth(180)
    t.fd(20)
    go(x+40,y)
    t.fd(40)
    go(x+50,y-59.5)
    t.fd(60)
    go(x+50,y-58)
    t.fd(60)




#making P:

def call_P(x,y):
    go(x,y)
    t.seth(270)
    t.seth(270)
    t.fd(100)
    t.right(90)
    t.fd(10)
    t.left(180)
    t.fd(40)
    t.left(180)
    t.fd(10)
    t.right(90)
    t.fd(40)
    t.up()
    t.fd(20)
    t.down()
    t.fd(40)
    t.right(90)
    t.fd(10)
    t.left(180)
    t.fd(40)
    t.seth(0)
    t.fd(100)
    t.circle(-20,90)
    
    t.fd(28)
    t.seth(180)
    t.fd(90)
    t.seth(270)
    t.fd(5)
    t.seth(0)
    t.fd(90)
    t.seth(90)
    t.fd(2)


#making y:
def call_Y(x,y):
    go(x,y)
    t.seth(0)
    t.fd(40)
    t.seth(180)
    t.fd(10)
    
    t.left(135)
    t.fd(46)
    go(x,y)
    t.seth(0)
    t.fd(10)
    t.right(42)
    t.fd(80)
    t.seth(270)
    t.fd(45)
    t.seth(180)
    t.fd(10)
    t.seth(0)
    t.fd(40)
    t.seth(180)
    t.fd(10)
    t.seth(90)
    t.fd(45)
    t.seth(45)
    t.fd(70)
    t.seth(0)
    t.fd(10)
    t.seth(180)
    t.fd(40)
    t.seth(0)
    t.fd(10)
    t.right(130)
    t.fd(40)
    t.seth(180)
    t.fd(27)
    



def call_D(x,y):
    go(x,y)
    t.seth(270)
    t.fd(100)
    t.seth(180)
    t.fd(10)
    t.seth(0)
    t.fd(50)
    t.circle(50,180)
    t.fd(60)
    t.seth(0)
    t.begin_fill()
    t.fillcolor('red')
    t.seth(270)
    t.fd(100)
    t.seth(0)
    t.fd(20)
    t.seth(90)
    t.fd(100)
    t.seth(180)
    t.fd(20)
    t.end_fill()
    go(325,25)
    t.seth(270)
    t.fd(60)
    t.seth(0)
    t.fd(10)
    t.circle(30,180)
    t.fd(10)
    t.seth(0)


#Happy birthday drawing: 

call_H(-600,220) 
call_A(-399,220)
call_P(-249,220)
call_P(-100,220)

call_Y(50,220)
t.speed('slow')
go(-490,-100)
t.write("B I R T H",font=('Castellar',108,'underline'))
call_D(300,45)
call_A(500,40)
call_Y(600,45)

go(-100,-330)
t.write("🎂Soumadip Santra❤️",font=('Algerian',70,'bold'),align='center',move=True)