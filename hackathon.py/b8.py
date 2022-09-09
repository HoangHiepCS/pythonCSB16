a = int(input("Input number of edge: "))
b = ((a-2)*180)/a
from turtle import*
while True:
    forward(40)
    left(180-b)
