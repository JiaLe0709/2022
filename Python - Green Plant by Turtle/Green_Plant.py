import turtle as tur 
tur.speed(0)
tur.color('#4d1919')
tur.width(5)

def go_to_pos(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()
    
def leaf(x):
    tur.width(1)
    tur.forward(20)
    tur.right(60)
    tur.begin_fill()
    tur.fillcolor('green')
    tur.circle(x/2,90)
    tur.forward(x/2)
    tur.left(127)
    tur.forward(x/2)
    tur.circle(x/2,90)
    tur.end_fill()
    tur.left(115)
    tur.width(0.1)
    tur.forward(x)
    tur.color('#bfff00')
    for i in range(4):
        tur.backward(x/4)
        tur.width(2/(4-i))
        tur.left(30)
        tur.forward(x/(7-i))
        tur.backward(x/(7-i))
        tur.right(60)
        tur.forward(x/(7-i))
        tur.backward(x/(7-i))
        tur.left(30)
    tur.width(5)
    tur.color('#4d1919')
    tur.backward(20)
    
def branches():
    for b in range(3):
        tur.seth(30*(b+1))
        go_to_pos(0,-250)
        n =12
        for i in range(n):
            angle = 45 if i %2 else -45
            tur.circle(500,4)
            tur.right(angle)
            leaf(80+((n-i)*2))
            tur.left(angle)
        leaf(80)
        
def pot():
    go_to_pos(2,-250)
    tur.seth(-90)
    tur.width(10)
    tur.begin_fill()
    tur.forward(30)
    tur.seth(0)
    tur.forward(30)
    tur.seth(-100)
    tur.forward(40)
    tur.seth(180)
    tur.forward(50)
    tur.seth(100)
    tur.forward(40)
    tur.seth(0)
    tur.forward(30)
    tur.end_fill()
    
branches()
pot()
tur.done()