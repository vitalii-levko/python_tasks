#!/usr/bin/python3

class Hypotenuse:

    @staticmethod
    def find_hypotenuse(x1, y1, x2, y2):
        return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

print(Hypotenuse.find_hypotenuse(0, 0, 3, 4))
