import turtle
import math

# Set the background color
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Creat turtle
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(10)

# Draw the front of the house
t.penup()
t.goto(-150, -120)
t.pendown()

# Draw rectangle with the given dimensions and color

color_rec = "blue"
width_rec = 100
height_rec = 110

t.fillcolor(color_rec)
t.begin_fill()
t.forward(width_rec)
t.left(90)
t.forward(height_rec)
t.left(90)
t.forward(width_rec)
t.left(90)
t.forward(height_rec)
t.left(90)
t.end_fill()

# Draw the door of the house
t.penup()
t.goto(-120, -120)
t.pendown()

color_rec = "light green"
width_rec = 40
height_rec = 60

t.fillcolor(color_rec)
t.begin_fill()
t.forward(width_rec)
t.left(90)
t.forward(height_rec)
t.left(90)
t.forward(width_rec)
t.left(90)
t.forward(height_rec)
t.left(90)
t.end_fill()

# Draw the front roof of the house
t.penup()
t.goto(-150, -10)
t.pendown()

# Draw Triangle for the roof
length_tri = 100
color_tri = "magenta"

t.fillcolor(color_tri)
t.begin_fill()
t.forward(length_tri)
t.left(135)
t.forward(length_tri / math.sqrt(2))
t.left(90)
t.forward(length_tri / math.sqrt(2))
t.left(135)
t.end_fill()

# Draw side of the house
t.penup()
t.goto(-50, -120)
t.pendown()

# Draw Parallelogram side of the house
width_para = 60
height_para = 110
color_para = "yellow"

t.fillcolor(color_para)
t.begin_fill()
t.left(30)
t.forward(width_para)
t.left(60)
t.forward(height_para)
t.left(120)
t.forward(width_para)
t.left(60)
t.forward(height_para)
t.left(90)
t.end_fill()

# Draw the window of the house
t.penup()
t.goto(-30, -60)
t.pendown()

width_para = 20
height_para = 30
color_para = "brown"

t.fillcolor(color_para)
t.begin_fill()
t.left(30)
t.forward(width_para)
t.left(60)
t.forward(height_para)
t.left(120)
t.forward(width_para)
t.left(60)
t.forward(height_para)
t.left(90)
t.end_fill()

# Draw side of the roof
t.penup()
t.goto(-50, -10)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(75)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(45)
t.end_fill()

# Draw the tree
# Tree base
t.penup()
t.goto(100, -130)
t.pendown()

color_tree_base = "brown"
width_tree_base = 20
height_tree_base = 40

t.fillcolor(color_tree_base)
t.begin_fill()
t.forward(width_tree_base)
t.left(90)
t.forward(height_tree_base)
t.left(90)
t.forward(width_tree_base)
t.left(90)
t.forward(height_tree_base)
t.left(90)
t.end_fill()

# Tree top
t.penup()
t.goto(65, -90)
t.pendown()

length_tree_top1 = 90
color_tree_top1 = "lightgreen"

t.fillcolor(color_tree_top1)
t.begin_fill()
t.forward(length_tree_top1)
t.left(135)
t.forward(length_tree_top1 / math.sqrt(2))
t.left(90)
t.forward(length_tree_top1 / math.sqrt(2))
t.left(135)
t.end_fill()

t.penup()
t.goto(70, -45)
t.pendown()

length_tree_top2 = 80
color_tree_top2 = "lightgreen"

t.fillcolor(color_tree_top2)
t.begin_fill()
t.forward(length_tree_top2)
t.left(135)
t.forward(length_tree_top2 / math.sqrt(2))
t.left(90)
t.forward(length_tree_top2 / math.sqrt(2))
t.left(135)
t.end_fill()

t.penup()
t.goto(75, -5)
t.pendown()

length_tree_top3 = 70
color_tree_top3 = "lightgreen"

t.fillcolor(color_tree_top3)
t.begin_fill()
t.forward(length_tree_top3)
t.left(135)
t.forward(length_tree_top3 / math.sqrt(2))
t.left(90)
t.forward(length_tree_top3 / math.sqrt(2))
t.left(135)
t.end_fill()

# Draw the Sun
t.penup()
t.goto(55, 110)
t.fillcolor("yellow")
t.pendown()
t.begin_fill()
t.circle(24)
t.end_fill()

# Sun rays
t.penup()
t.goto(55, 134)
t.pendown()

length_rays = 25
radius = 24

for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length_rays)
    t.penup()
    t.backward(length_rays + radius)
    t.left(90)

t.right(45)
length_rays = 15
radius = 24

for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length_rays)
    t.penup()
    t.backward(length_rays + radius)
    t.left(90)
t.left(45)

# Put the turte down to the front door
t.penup()
t.goto(-100, -150)
t.left(90)
t.color("black")
turtle.done()
