import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("lightgreen")

def circles(color, radius):

    t.fillcolor(color)

    t.begin_fill()

    t.circle(radius)

    t.end_fill()

t.up()
t.setpos(-35, 95)
t.down
circles('black', 15)

t.up()
t.setpos(35, 95)
t.down()
circles('black', 15)

t.up()
t.setpos(0, 35)
t.down()
circles('white', 40)

t.up()
t.setpos(-18, 75)
t.down
circles('black', 8)

t.up()
t.setpos(18, 75)
t.down()
circles('black', 8)

t.up()
t.setpos(-18, 77)
t.down()
circles('white', 4)

t.up()
t.setpos(18, 77)
t.down()
circles('white', 4)

t.up()
t.setpos(0, 55)
t.down
circles('black', 5)

t.up()
t.setpos(0, 55)
t.down()
t.right(90)
t.circle(5, 180)
t.up()
t.setpos(0, 55)
t.down()
t.left(360)
t.circle(5, -180)
t.hideturtle()