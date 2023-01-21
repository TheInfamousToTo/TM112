from turtle import *
bgcolor('red')
forw = 1
speed(200)
while True:
    if abs(pos()) <150:
        color('yellow', 'blue')
    else:
        color('blue', 'yellow')
    begin_fill()
    forward(forw)
    right(90)
    right(1)
    forw += 1
    if abs(pos()) > 300:
        break
end_fill()
done()

