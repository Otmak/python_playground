# Name : Diana Sokol, Gail Flynn & Otuma Kazelausha
# Date : 6/04/2020
# Description : Final Project Turtle Escape Game

import random
import turtle

# Approximate size of turtle objects in pixels
BODY_SIZE = 80

# Half if the body size for collision detection with the edge of the screen
HALF_BODY_SIZE = BODY_SIZE / 2

# if enemies get this close to friend there is collision
COLLISION_DISTANCE = 5

# The window size
SIZE = 500

# inner boundary within window for reversing the direction of enemies
LOWER_BOUND = -SIZE / 2 + HALF_BODY_SIZE
UPPER_BOUND = SIZE / 2 - HALF_BODY_SIZE
print(LOWER_BOUND, UPPER_BOUND)

# changing the turtle size
# turtle.shapesize(3, 3)
# creating a screen
win = turtle.Screen()
win.delay(9)
win.tracer(2)
win.setup(width=500, height=500)  # setting the window to 500 x 500
win.title('Turtle Escape')  # adding title

# creating our main turtle 'friend'and color lime at the lower right-hand corner of the window
friend = turtle.Turtle()
friend.penup()
friend.shape('turtle')
friend.color('lime')
friend.shapesize(3, 3)
friend.goto(win.window_width() / 2 - BODY_SIZE, - win.window_height() / 2 + BODY_SIZE)
border = win.window_width() / 2  # Since the Width/Height is 500 and pac starts at 0,0 the edge will be '500/2' = 250


def create_turtle():  # Function Creates a turtle with properties(color='red',shape='Ball', starts in random direction)
    pac = turtle.Turtle()
    pac.color('red')
    pac.shape('circle')
    pac.penup()
    pac.shapesize(3, 3)
    pac.setheading(random.randrange(0, 360))

    return pac  # returning our turtle


def move(name):  # Function will Checks to see if the turtle has passed the edge
    # If so, moves it backwards and changes its direction.

    x, y = name.position()  # Setting x and y to the position of 'pac' based on X and Y axis
    if x > border or y > border or y < -border or x < -border:  # This checks if top & right side of location is >= 250 & calls move()
        name.forward(-5)
        name.setheading(random.randrange(360))
    #  the if statements will move the ball  back 5 pixels and then change to random direction


def up():
    friend.penup()
    friend.setheading(90)  # setting the direction
    friend.forward(45)  # moving forward 45 pixels
    friend.pendown()


def down():
    friend.penup()
    friend.setheading(270)  # setting the direction
    friend.forward(45)  # moving forward 45 pixels
    friend.pendown()


def left():
    friend.penup()
    friend.setheading(180)  # setting the direction
    friend.forward(45)  # moving forward 45 pixels
    friend.pendown()


def right():
    friend.penup()
    friend.setheading(0)  # setting the direction
    friend.forward(45)  # moving forward 45 pixels
    friend.pendown()


# detect whether friend has collided with enemies (or vice-versa)
def collision(friend, enemies):
    # initialize is_collision to False
    is_collision = False
    for enemy in enemies:
        how_far = friend.distance(enemy.pos())
        # if how_far is within collision distance set is_collision to True
        if how_far <= COLLISION_DISTANCE:
            is_collision = True
    return is_collision  # return collisions state


def reached_opposite_corner(friend):
    # initialize reached corner (opposite corner) to false
    reached_corner = False
    x, y = friend.pos()
    if x < LOWER_BOUND and y > UPPER_BOUND:
        # friend has reached corner, set variable to true
        reached_corner = True
    return reached_corner  # return whether friend reached upper left corner


# creating an empty list of enemies
enemies = []
# looping for 5 times, creating a turtle, appending to list
for i in range(5):
    enemies.append(create_turtle())

# move friend using keyboard arrows
win.onkey(up, "Up")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(down, "Down")
win.listen()

# Repeat until a collision or friend as reached upper left corner
while True and not collision(friend, enemies) and not reached_opposite_corner(friend):
    for enemy in enemies:
        enemy.forward(5)
        move(enemy)

# Checking whether player won or not
if reached_opposite_corner(friend):
    print("Game over: Your friend made it!")
elif collision(friend, enemies):
    print("Game over: Your friend is now turtle soup!")
else:
    print("Game over: Unknown reason: Programming error!")
