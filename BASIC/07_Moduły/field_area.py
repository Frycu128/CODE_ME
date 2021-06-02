import math


def circle(r):
    circle_field = math.pi * r**2
    return circle_field


def rectangle(a, b):
    rectangle_field = a * b
    return rectangle_field


def triangle(a, h):
    triangle_field = 0.5 * a * h
    return triangle_field


def delta(a, b, c):
    return b**2 - 4 * math.pow(a, c)
