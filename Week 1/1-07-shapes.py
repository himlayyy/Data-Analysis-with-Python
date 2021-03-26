#!/usr/bin/env python 3
import math


def triangle():
    base = int(input("Give base of triangle: "))
    height = int(input("Give height of triangle: "))
    print(f"Area is {(base*height)/2:.6f}")


def rectangle():
    length = int(input("Give length of rectangle: "))
    width = int(input("Give width of rectangle: "))
    print(f"Area is {length*width:.6f}")


def circle():
    radius = int(input("Give radius of circle: "))
    print(f"Area is {math.pi*(radius**2):.6f}")


while True:
    shape = str(input("Choose a shape (triangle, rectangle, circle):"))
    if not shape:
        break
    elif shape.casefold() == "triangle":
        triangle()
    elif shape.casefold() == "rectangle":
        rectangle()
    elif shape.casefold() == "circle":
        circle()
    else:
        print("Unknown shape!")
