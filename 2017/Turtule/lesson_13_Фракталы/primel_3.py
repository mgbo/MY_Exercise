
# -*- coding: utf-8 -*-
import turtle           
import time
import math

def gen(size, n):   # Первый отрезок обозначим как АF
  t.fd(size)
  A(size, n-1)
  
def A(size, n):
  if n==0:          # A не рисуем никак
    return
                    # из А получаем A+BF+
  A(size, n-1)      # A
  t.right(90)       # +
  B(size, n-1)      # B
  t.fd(size)        # F
  t.right(90)       # +
    
def B(size, n):
  if n==0:          # B не рисуем никак
    return
                    # из В получаем &#8722;FA&#8722;B
  t.left(90)        # -
  t.fd(size)        # F
  A(size, n-1)      # A
  t.left(90)        # -
  B(size, n-1)      # B
  
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
t.color('blue')

gen(10, 10)     # правила применили глубиной 10

t.hideturtle()
turtle.done()
