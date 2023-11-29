import turtle
a=turtle.Turtle()
a.speed(0)
a.pu()
a.goto(300,300)
a.pd()


for i in range(4):
    a.right(90)
    a.fd(600)

    
a.goto(-300,300)
a.color("red")
a.begin_fill()
for i in range(4):     
    a.fd(240)
    a.right(90)
a.end_fill()
a.pu()


a.goto(60,300)
a.color("green")
a.begin_fill()
for i in range(4):
    a.fd(240)
    a.right(90)
a.end_fill()


a.goto(60,-60)
a.color("yellow")
a.begin_fill()
for i in range(4):
    a.fd(240)
    a.right(90)
a.end_fill()


a.goto(-300,-60)
a.color("blue")
a.begin_fill()
for i in range(4):
    a.fd(240)
    a.right(90)
a.end_fill()
a.color("black")


x=300
a.goto(-60,x)
a.pd()
for i in range(6):
    for i in range(3):
        for i in range(4):
            a.fd(40)
            a.right(90)
        a.fd(40)
    x-=40
    a.pu()
    a.goto(-60,x)
    a.pd()


x=-60
a.goto(-60,x)
a.pd()
for i in range(6):
    for i in range(3):
        for i in range(4):
            a.fd(40)
            a.right(90)
        a.fd(40)
    x-=40
    a.pu()
    a.goto(-60,x)
    a.pd()


a.pu()
x=60
a.goto(-300,x)
a.pd()
for i in range(3):
    for i in range(6):
        for i in range(4):
            a.fd(40)
            a.right(90)
        a.fd(40)
    x-=40
    a.pu()
    a.goto(-300,x)
    a.pd()


a.pu()
x=60
a.goto(60,x)
a.pd()
for i in range(3):
    for i in range(6):
        for i in range(4):
            a.fd(40)
            a.right(90)
        a.fd(40)
    x-=40
    a.pu()
    a.goto(60,x)
    a.pd()


a.pu()
a.goto(60,60)
a.pd()
a.color("green")
a.begin_fill()
a.goto(-60,60)
a.goto(0,0)
a.goto(60,60)
a.end_fill()


a.color("yellow")
a.begin_fill()
a.goto(60,-60)
a.goto(0,0)
a.goto(60,60)
a.end_fill()


a.goto(60,-60)
a.color("blue")
a.begin_fill()
a.goto(-60,-60)
a.goto(0,0)
a.goto(60,-60)
a.end_fill()


a.goto(-60,-60)
a.color("red")
a.begin_fill()
a.goto(-60,60)
a.goto(0,0)
a.goto(-60,-60)
a.end_fill()


a.color("black")
for i in range(4):
    a.goto(60,60)
    a.goto(-60,-60)
a.goto(-60,60)
for i in range(4):
    a.goto(60,-60)
    a.goto(-60,60)


a.pu()
a.goto(-260,60)
a.pd()
a.color("red")
a.begin_fill()
for i in range(4):
    a.fd(40)
    a.right(90)
a.end_fill()
a.goto(-260,20)
for i in range(5):
    a.begin_fill()
    for i in range(4):
        a.fd(40)
        a.right(90)
    a.end_fill()
    a.fd(40)


a.pu()
a.goto(220,-60)
a.color("yellow")
a.begin_fill()
for i in range(4):
    a.fd(40)
    a.left(90)
a.end_fill()
a.goto(60,-20)
for i in range(5):
    a.begin_fill()
    for i in range(4):
        a.fd(40)
        a.left(90)
    a.end_fill()
    a.fd(40)


a.color("green")
a.goto(20,260)
a.begin_fill()
for i in range(4):
    a.fd(40)
    a.right(90)
a.end_fill()
x=260
a.goto(-20,x)
for i in range(5):
    a.begin_fill()
    for i in range(4):
        a.fd(40)
        a.right(90)
    a.end_fill()
    x-=40
    a.goto(-20,x)


a.color("blue")
a.goto(-60,-260)
a.begin_fill()
for i in range(4):
    a.fd(40)
    a.left(90)
a.end_fill()
x=-260
a.goto(-20,x)
for i in range(5):
    a.begin_fill()
    for i in range(4):
        a.fd(40)
        a.left(90)
    a.end_fill()
    x+=40
    a.goto(-20,x)


x=25
a.color("white")
a.goto(-140,120)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(-140,200)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(-220,200)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(-220,120)
a.begin_fill()
a.circle(x)
a.end_fill()


a.goto(140,120)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(140,200)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(220,120)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(220,200)
a.begin_fill()
a.circle(x)
a.end_fill()


a.goto(140,-160)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(140,-240)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(220,-160)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(220,-240)
a.begin_fill()
a.circle(x)
a.end_fill()



a.goto(-140,-160)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(-140,-240)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(-220,-160)
a.begin_fill()
a.circle(x)
a.end_fill()
a.goto(-220,-240)
a.begin_fill()
a.circle(x)
a.end_fill()


a.pu()
a.goto(300,300)
a.pd()
a.color("black")


for i in range(8):
    a.right(90)
    a.fd(600)


for i in range(2):
    x=300
    a.goto(-60,x)
    a.pd()
    for i in range(6):
        for i in range(3):
            for i in range(4):
                a.fd(40)
                a.right(90)
            a.fd(40)
        x-=40
        a.pu()
        a.goto(-60,x)
        a.pd()


    x=-60
    a.goto(-60,x)
    a.pd()
    for i in range(6):
        for i in range(3):
            for i in range(4):
                a.fd(40)
                a.right(90)
            a.fd(40)
        x-=40
        a.pu()
        a.goto(-60,x)
        a.pd()


    a.pu()
    x=60
    a.goto(-300,x)
    a.pd()
    for i in range(3):
        for i in range(6):
            for i in range(4):
                a.fd(40)
                a.right(90)
            a.fd(40)
        x-=40
        a.pu()
        a.goto(-300,x)
        a.pd()


    a.pu()
    x=60
    a.goto(60,x)
    a.pd()
    for i in range(3):
        for i in range(6):
            for i in range(4):
                a.fd(40)
                a.right(90)
            a.fd(40)
        x-=40
        a.pu()
        a.goto(60,x)
        a.pd()
    a.pu()


a.hideturtle()
turtle.done()


