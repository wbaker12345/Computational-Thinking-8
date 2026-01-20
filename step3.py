# Section 1 - Your code
from utils import *
set_background("logo")

s1 = create_sprite("mariners", 0, -60)
s2 = create_sprite("drakey", 0, 70)
s2 = create_sprite("william", 0, 0)
#s2 = create_sprite("", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Will",font = ("Arial", 70, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()