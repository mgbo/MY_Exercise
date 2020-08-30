"""
h, a, b=int(input()), int(input()), int(input())

hh=h-a
k=a-b

print((1+hh)//k + (hh%(k+k-1))//k)
"""

days = 0
nights = 0
h = int(input())
a = int(input())
b = int(input())

while a * days - b * nights <= h:
    if a * days - b * (nights - 1) == h:
        print(days)
    else:
        pass
    days += 1
    nights += 1