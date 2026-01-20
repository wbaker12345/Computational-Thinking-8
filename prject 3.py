import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-350
y1 =200
x2 =-350
y2 =-100
x3 =-350
y3 =-0
x4 =-350
y4 =100


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("ric flair")
t1 = create_sprite("drake",x1,y1)
t2 = create_sprite("carti",x2,y2)
t3 = create_sprite("mata",x3,y3)
t4 = create_sprite("spunge",x4,y4)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - the drake sprite is fastes beacuse its max speed it set to 50 the slowest is carti beacuse it goes at the speed of 10 everytime
for i in range(37):
    x1 += random.randint(-10, 50)
    x2 += 10
    x3 +=15
    x4 += random.randint(1,35)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("drake wins")
elif x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 2 wins!")
elif x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("carti wins seeyah")
elif x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Chicken snugg wins")

turtle.exitonclick()