import turtle, time, random
from utils import *
#every time tou click the space key you gain 1 fain and want you get enough fans you can buy a new album. Play to see how many albums you can buy
# Section 1 - setup
# TODO - set a background using 
set_background("drakeback")
t1 =create_sprite("talk",-350, 150)

# TODO - create at least two variables and set their starting value. ex: cookies = 0
fans = 0
cost = 10
album = 0
song = 0


# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_fans () :
    global fans
    fans += 1
    x = random.randint (200,300)
    y = random.randint (-250,200)
    create_sprite("fans", x, y)
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(make_fans, "space")



# TODO - make a second control
def make_album() :
    global album, fans, cost
    if fans >= cost:
        fans = fans - cost
        cost = cost +5
        album+=1
        x = -200 + 15 *fans
        y = -150
        create_sprite("album", x, y)
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(make_album, "c")




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    t1.clear()
    t1.write(f"fans: {fans}\ncost: {cost}\nalbum: {album}", font=("Arial",30,"normal"))
    t1.color("pink")
    # TODO - put any repeating actions here
    time.sleep(0.01)
    window.update() 