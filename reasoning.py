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
        # self.input = inp

        patterns = [method for method in dir(self) if callable(getattr(self, method)) and method.startswith("pattern")]

        self.patterns = patterns
    
    def random_pattern(self):
        patterns = self.patterns
        method = random.choice(patterns)

        return getattr(self, method)

    def generate_question(self, pattern_index=-1):
        patterns = self.patterns
        pattern = patterns[pattern_index] if pattern_index != -1 else self.random_pattern()

        part1 = pattern()

        part2 = pattern()

        answer = pattern()

        question = "{}::{}".format(":".join(part1), ":".join(part2))

        options = [answer] + [o for o in self.generate_random_options(3, len(answer))]

        random.shuffle(options)

        options = [":".join(o) for o in options]

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

        a = random.randint(1, 10)
        b = random.randint(1, 10)

        y = x*a + b

        return (x, y)


