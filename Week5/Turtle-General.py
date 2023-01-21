import turtle as t
#t = turtle.Turtle()
t.pensize(2)


t.color('green', 'red')
t.begin_fill()
t.setx(0)
t.circle(50)
t.end_fill()


t.color('red', 'yellow')
t.begin_fill()
t.pu()
t.setx(110)
t.pd()
t.circle(50)
t.end_fill()

t.pu()
t.setx(0)
t.sety(-110)
t.color('blue', 'pink')
t.begin_fill()
t.pd()
t.circle(50)
t.end_fill()

t.color('green', 'blue')
t.begin_fill()
t.pu()
t.setx(110)
t.sety(-110)
t.pd()
t.circle(50)
t.end_fill()





