import random
from utils import *

class ReasoningQuestions:
    index = {
        "0": {
            "name": "Random pattern",
            "method": "random_pattern"
        },
        "1": {
            "name": "ax + b = y",
            "method": "pattern_1"
        }
    }

    def __init__(self):

        self.a = None
        self.b = None

        patterns = [method for method in dir(self) if callable(getattr(self, method)) and method.startswith("pattern")]

        self.patterns = patterns

    def _set_random_constants(self):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)

        return True
    
    def _clear_constants(self):
        self.a = None
        self.b = None

        return True
    
    def random_pattern(self):
        patterns = self.patterns
        method = random.choice(patterns)

        return getattr(self, method)

    def generate_question(self, pattern_index=0):
        patterns = self.patterns
        
        self._set_random_constants()

        print("a: {}, b: {}".format(self.a, self.b))

        pattern = getattr(self, self.index[str(pattern_index)]['method'])

        part1 = pattern()

        part2 = pattern()

        answer = pattern()

        question = "{}\n{}\n".format(part1, part2)

        options = [answer] + [o for o in self.generate_random_options(3, len(answer))]

        random.shuffle(options)

        self._clear_constants()

        return [question, options, answer]

    def generate_random_options(self, num, params=2):
        options = []

        for i in range(num):
            x = random.randint(1, 10)
            y = random.randint(1, 10)

            if params == 3:
                z = random.randint(1, 10)
                options.append((x,y,z))
            else:
                options.append((x,y))

        return options

    def pattern_1(self):
        x = random.randint(1, 10)

        a = self.a
        b = self.b

        y = x*a + b

        return (x, y)


