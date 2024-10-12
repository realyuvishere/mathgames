import random
from utils import *

class MathQuestions:
    index = {
        "1": {
            "name": "Guess the square root",
            "method": "guess_square_root"
        },
        "2": {
            "name": "Guess the cube root",
            "method": "guess_cube_root"
        },
        "3": {
            "name": "Guess the Pythagorean triplet",
            "method": "guess_pythagorean_triplet"
        }
    }

    def __init__(self):
        pass

    def guess_square_root(self):
        num = random.randint(1, 30)

        sqr = num**2

        return [sqr, num]

    def guess_cube_root(self):
        num = random.randint(1, 30)

        cube = num**3

        print("printing cubes")

        return [cube, num]

    def guess_pythagorean_triplet(self):

        def generate_triplet():
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            c = math.sqrt(a**2 + b**2)

            if c == int(c):
                return [a, b, int(c)]
            else:
                return generate_triplet()
        
        triplet = generate_triplet()

        random.shuffle(triplet)

        answer = triplet.pop()        

        return [triplet, answer]

