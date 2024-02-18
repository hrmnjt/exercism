def triangle(sides):
    return (sides[0] + sides [1] >= sides[2]) and (sides[1] + sides [2] >= sides[0]) and (sides[2] + sides [0] >= sides[1])


def equilateral(sides):
    return sides[0] == sides[1] == sides [2] != 0 if triangle(sides) else False


def isosceles(sides):
    return (sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[2] == sides[0]) if triangle(sides) else False


def scalene(sides):
    return (sides[0] != sides[1]) and (sides[1] != sides [2]) and (sides[0] != sides[2]) if triangle(sides) else False
