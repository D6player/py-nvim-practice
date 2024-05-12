""" Quick interpolated noise implementation """

import random
from math import floor, ceil

class InterpolatedNoise():
    def __init__(self, width: int, height: int, depth: int, size: int):
        # random.seed(9004) # temporary
        self.noise = [
            [
                random.random() for _ in range(width)
            ] for _ in range(height)
        ]

        self.width = width
        self.height = height
        self.depth = depth
        self.size = size
        self.correction = sum(1/2**o for o in range(size, depth+1))

    def get_interpolated_noise(self, x: int, y: int) -> float:
        tap = 0
        
        for octave in range(self.size, self.depth+1):
            xp = x * octave/self.width
            yp = y * octave/self.height

            (R0, R1, R2, R3) = self.__get_noises(octave, xp, yp)
            (w, h) = map((lambda i: i - floor(i)), (xp, yp))

            I0 = self.__interpolate(R0, R1, w)
            I1 = self.__interpolate(R2, R3, w)

            tap += self.__interpolate(I0, I1, h) / 2**octave
        
        return tap / self.correction

    def __get_noises(self, octave: int, xp: float, yp: float):
        (X0, Y0, X1, Y1) = InterpolatedNoise.__get_corners(xp, yp)
        (X0, X1) = map((lambda X: (X*self.width)//octave), (X0, X1))
        (Y0, Y1) = map((lambda Y: (Y*self.height)//octave), (Y0, Y1))
        
        return (
            self.noise[Y0][X0],
            self.noise[Y0][X1-1],
            self.noise[Y1-1][X0],
            self.noise[Y1-1][X1-1],
        )

    @staticmethod
    def __get_corners(xp: float, yp: float):
        return (
            floor(xp), floor(yp),
            ceil(xp), ceil(yp),
        )

    def __interpolate(self, a, b, x) -> float:
        return a + (b - a)*InterpolatedNoise.__ease_function(x)

    @staticmethod
    def __ease_function(x: float) -> float:
        return 2*x**2 if x < 0.5 else 1-(2-2*x)**2 /2
        
