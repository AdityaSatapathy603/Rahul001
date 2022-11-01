import turtle
    
#turtle.bgcolor("black")
#turtle.pensize(2)
#turtle.speed(3)

#for i in range(6):
    #for colours in ["red","yellow","blue","green","pink","cyan","white"]:
        #turtle.color(colours)
        #turtle.circle(100)
        #turtle.left(10)

#turtle.hideturtle()


#t = turtle.Turtle()
#turtle.bgcolor("black")
#t.pencolor("green")
#a = 0
#b = 0
#t.speed(0)
#t.penup()
#t.goto(0,200)
#t.pendown()
#while True:
    #t.forward(a)
    #t.right(b)
    #a+=3
    #b+=1
    #if b == 340:
        #break
    #t.hideturtle()

form = 1
turtle.bgcolor("black")
turtle.pensize(1)
turtle.pencolor("white")
turtle.speed(0)
while True:
    turtle.forward(form)
    turtle.left(120)
    turtle.left(1)
    form += 1
turtle.done()
