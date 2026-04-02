import math
from turtle import *


class Heart:
    def __init__(self):
        self.run()

    def hearta(self,k):
        return 15 * math.sin(k) ** 3

    def heartb(self,k):
        return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

    def run(self):
        speed(0)
        bgcolor("black")
        for i in range(6000):
            goto(self.hearta(i) * 20, self.heartb(i) * 20)
            for j in range(5):
                color("red")
                goto(0, 0)
        done()
Heart()