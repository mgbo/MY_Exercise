
# -*- coding: utf-8 -*-
# чтобы можно было писать русские буквы и иероглифы

import turtle         # познакомили программу с пакетом turtle (черепаха)

t = turtle.Turtle()   # сделали черепаху, назвали черепаху t

t.color('red', 'yellow')  # линия - красный, внутри - желтый

t.begin_fill()        # начинаем рисовать замкнутую фигуру

t.forward(75)         # нарисуем квадрат
t.left(90)            
t.forward(75)         
t.left(90)            
t.forward(75)         
t.left(90)            
t.forward(75)         
t.left(90)      

t.end_fill()          # заканчиваем рисовать фигуру

turtle.mainloop()     # чтобы окно не закрывалось, на repl.it не нужно
