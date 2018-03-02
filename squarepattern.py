import turtle
import random

t = turtle.Turtle()
t.ht()
t.pu()
turtle.tracer(10,0)
t.speed(0)
t.setx(-400)
t.sety(-400)
def sq(turt,l,x):
  for each in range(4):
    temp = random.randrange(0,2)
    if temp == 1:
      turt.pu()
    turt.right(90)
    turt.forward(l)
    turt.pd()
  if x == 0:
    turt.right(135)
    turt.forward(l*1.41)
  elif x == 1:
    turt.left(180)
    turt.forward(l)
    turt.left(135)
    turt.forward(l*1.41)
  elif x == 2:
    turt.right(135)
    turt.forward(l*1.41)
    turt.right(135)
    turt.forward(l)
    turt.right(135)
    turt.forward(l*1.41)
  else:
    pass
for x in range(-400,400,20):
  for y in range(400,-400,-20):
    for each in range(1):
      t.sety(y)
      t.setx(x)
      t.seth(0)
      t.pd()
      r = random.randrange(0,4)
      sq(t,20,r)
      t.pu()
  t.sety(y)
