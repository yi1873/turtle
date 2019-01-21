#-*-coding:utf-8-*-

from turtle import *

#setup(450,535,None,None)

def wall():
	penup()
	speed(0)
	seth(180)
	fd(40)
	seth(90)
	fd(255)
	pendown()
	seth(-90)
	pensize(5)
	pencolor("#915442")
	fd(450)
	print(position())
	penup()
	

def nut():
	penup()
	pencolor("#915442")
	fillcolor("chocolate")
	goto(-40.00,-110.00)
	pendown()
	begin_fill()
	seth(20)
	for i in range(1,7):
		fd(9)
		left(7)
	for i in range(1,4):
		fd(10)
		left(13)
	seth(120)
	for i in range(1,7):
		fd(5)
		left(13)
	for i in range(1,7):
		fd(5)
		left(5)
	end_fill()
	penup()
	goto(-40.00,-103.00)
	pendown()
	fillcolor("sandybrown")
	begin_fill()
	seth(24)
	for i in range(1,7):
		fd(9)
		left(7)
	for i in range(1,4):
		fd(9)
		left(13)
	seth(120)
	for i in range(1,5):
		fd(5)
		left(19)
	for i in range(1,7):
		fd(5)
		left(5)
	end_fill()
	penup()
	
def body():
	penup()
	goto(-40.00,-190)
	pendown()
	pencolor("#915442")
	pensize(3)
	fillcolor("#fff699")
	begin_fill()
	seth(0)
	fd(8)
	print(position())
	seth(60)
	for i in range(1,7):
		fd(3)
		right(9)
	for i in range(1,4):
		fd(4)
		right(4)
	penup()
	goto(-30.00,-190.00)
	pendown()
	seth(-30)
	for i in range(1,5):
		fd(3)
		left(12)
	print(position())
	seth(60)
	for i in range(1,4):
		fd(2)
		right(10)
	penup()
	goto(-18.58,-193.43)
	pendown()
	seth(0)
	fd(4)
	for i in range(1,4):
		fd(3)
		left(9)
	print(position())
	for i in range(1,3):
		fd(3)
		left(9)
	penup()
	goto(-5.76,-192.03)
	pendown()
	seth(-40)
	for i in range(1,3):
		fd(1)
		left(20)
	fd(8)
	seth(10)
	for i in range(1,9):
		fd(3)
		left(7)
	seth(70)
	fd(25)
	circle(25,15)
	seth(95)
	fd(35)
	circle(-18,25)
	seth(85)
	fd(30)
	for i in range(1,21):
		fd(5)
		left(7)
	end_fill()
	penup()
	goto(-32.00,-190.00)
	pendown()
	begin_fill()
	seth(60)
	for i in range(1,7):
		fd(3)
		right(9)
	for i in range(1,4):
		fd(4)
		right(4)
	end_fill()
	penup()
	goto(-27.00,-187.50)
	pendown()
	pencolor("#fff699")
	pensize(4.5)
	goto(-5.00,-180.0)
	penup()

def marginal():
    goto(-40,100)
    pencolor("#915442")
    fillcolor("#fff699")
    begin_fill()
    pendown()
    seth(15)
    fd(13)
    pencolor("#bda537")#这是耳朵边缘色
    seth(-100)
    pensize(3)
    fd(10)
    goto(-27.44,103.36)
    seth(70)
    pencolor("#915442")
    for i in range(4):
        fd(15)
        rt(5)
    for i in range(3):
        fd(17)
        rt(8)
    seth(-45)
    fd(3)
    seth(-100)
    fd(15)
    for i in range(8):
        rt(1)
        fd(1)
    seth(-108)
    fd(20)
    for i in range(3):
        fd(19)
        rt(9)
    pencolor("#915442")
    fd(8)
    penup()
    goto(3.46,96.21)
    pendown()
    pensize(4)
    seth(-10)
    fd(15)
    pensize(3)
    circle(-40,30)
    pensize(4)
    fd(10)
    pensize(3)
    circle(30,20)
    for i in range(5):
        fd(1.5)
        lt(2)
    pensize(2)
    seth(0)
    fd(5)
    pensize(3)
    seth(-160)
    circle(-80,10)
    pensize(2)
    fd(4)
    penup()
    lt(180)
    fd(4)
    pendown()
    seth(-30)
    pensize(3)
    fd(20)
    circle(-1,140)
    fd(8)
    seth(-30)
    pencolor("#d06521")
    circle(-20,45)
    penup()
    pencolor("#915442")
    goto(61.53,54.30)
    pendown()
    seth(10)
    pensize(4)
    fd(50)#从这开始耳朵要涂棕色
    print(position())
    for i in range(5):
        fd(10)
        rt(3)
    seth(-10)
    pensize(3)
    for i in range(9):
        fd(1.5)
        rt(20)
    lt(55)
    circle(-90,30)#涂到这里为止
    circle(-120,25)
    seth(110)
    pensize(1)
    fd(3)
    pensize(4)
    seth(-80)
    fd(25)
    for i in range(10):
        fd(2)
        rt(2)
    for i in range(5):
        fd(3)
        rt(3)
    fd(40)#到达了脸红色涂色的右侧边缘
    circle(-20,60)
    circle(-10,40)
    lt(25)
    fd(64.91)
    end_fill()
    
    penup()
		

def eyes():
    goto(-38,10)
    seth(45)
    pendown()
    begin_fill()
    pencolor("#6b2a18")
    fillcolor("#6b2a18")
    circle(50,30)
    circle(7,170)
    end_fill()
    goto(-34,39)
    pencolor("#fffcea")
    dot(5)
    penup()
    goto(-50,100)
    
    penup()
    pencolor("#743212")
    goto(45,-35)
    pendown()
    seth(50)
    begin_fill()
    fillcolor("#6b2a18")
    circle(50,30)
    circle(6,170)
    rt(25)
    circle(50,25)
    circle(7,30)
    circle(6,35)
    circle(7,45)
    goto(45,-35)
    end_fill()
    penup()
    goto(45,-9)
    pendown()
    pencolor("#fffcea")
    dot(5)
    penup()
    hideturtle()
        
def printleft():
    penup()
    goto(-27.44,103.36)
    fillcolor("#8b3c15")
    seth(70)
    pencolor("#915442")
    for i in range(3):
        fd(15)
        rt(5)
    begin_fill()
    for i in range(1):
        fd(15)
        rt(5)
    for i in range(3):
        fd(17)
        rt(8)
    seth(-45)
    fd(3)
    seth(-100)
    fd(15)
    for i in range(8):
        rt(1)
        fd(1)
    seth(-108)
    fd(20)
    for i in range(1):
        fd(19)
        rt(9)
    seth(95)
    circle(60,20)
    circle(10,70)
    end_fill()
    penup()

def rightprint():
    goto(61.53,54.30)
    pendown()
    seth(10)
    pensize(4)
    fd(50)
    fillcolor("#8b3c15")
    begin_fill()
    for i in range(5):
        fd(10)
        rt(3)
    seth(-10)
    for i in range(9):
        fd(1.5)
        rt(20)
    lt(55)
    circle(-90,30)
    circle(-120,7)
    seth(60)
    circle(40,30)
    circle(15,40)
    penup()
    end_fill()

def hand():
	penup()
	goto(16,-80)
	pencolor("#915442")
	pensize(3)
	fillcolor("#fff699")
	pendown()
	begin_fill()
	seth(100)
	fd(10)
	circle(10,30)
	fd(15)
	circle(10,40)
	fd(10)
	seth(300)
	fd(5)
	seth(170)
	fd(7)
	seth(280)
	fd(7)
	seth(170)
	fd(5)
	seth(250)
	fd(7)
	for i in range(1,6):
		fd(0.5)
		left(10)
	seth(-70)
	fd(15)
	circle(30,10)
	for i in range(1,5):
		fd(7)
		left(4)
	end_fill()
	pendown()

def nose():
	penup()
	goto(2,-15)
	pendown()
	pencolor("#915442")
	dot(4)
	penup()

        
wall()
body()
marginal()
nut()
printleft()
rightprint()
hand()
nose()
eyes()

done()

