from turtle import *
color('red','black')
speed(1000)
begin_fill()
while True:
    forward(700)
    left(179.9)
    if abs(pos()) < 1:
        break
end_fill()
done()
