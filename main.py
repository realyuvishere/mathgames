import sys
import random
import math

python_version = sys.version_info[0]


def print_(str):
    if python_version < 3:
        print str
    else:
        print(str)




class ReasoningQuestions:
    index = {
        "1": {
            "name": "ax + b = y",
            "method": "pattern_1"
        }
    }

    def __init__(self):
        # self.input = inp

        patterns = [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith("__")]
        patterns.remove("random_pattern")
        patterns.remove("generate_question")

        self.patterns = patterns
    
    def random_pattern(self):
        patterns = self.patterns
        method = random.choice(patterns)

        return getattr(self, method)

    def generate_question(self, pattern_index):
        patterns = self.patterns
        pattern = patterns[pattern_index] if pattern_index != -1 else self.random_pattern()

        part1 = pattern()

        part2 = pattern()

        answer = pattern()

        question = "{}::{}".format(":".join(part1), ":".join(part2))

        options = [answer] + [o for o in self.generate_random_options(3, len(answer))]

        options = random.shuffle(options)

        options = [":".join(o) for o in options]

        return (question, options, answer)

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

        return (num, sqr)

    def guess_cube_root(self):
        num = random.randint(1, 30)

        cube = num**3

        return (num, cube)

    def guess_pythagorean_triplet(self):

        def generate_triplet():
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            c = math.sqrt(a**2 + b**2)

            if c == int(c):
                return (a, b, int(c))
            else:
                return generate_triplet()
        
        triplet = generate_triplet()

        triplet = random.shuffle(triplet)

        answer = triplet.pop()        

        return (triplet, answer)




class App:
    def __init__(self):
        self.name = "App"
        self.input = ""
        self.levels = {
            "0": {
                "name": "Main Menu",
                "class": self,
                "items": {
                    "0": {
                        "name": "Index",
                        "method": "display_index",
                    },
                    "1": {
                        "name": "Reasoning",
                        "method": "start_reasoning",
                    },
                    "2": {
                        "name": "Maths",
                        "method": "start_maths",
                    }
                }
            },
            "1": {
                "name": "Reasoning",
                "class": ReasoningQuestions,
                "options": ReasoningQuestions.index,
            },
            "2": {
                "name": "Maths",
                "class": MathQuestions,
                "options": MathQuestions.index,
            }
        }

        self.level = 0

    def read_input(self):
        print_('-'*20)
        print_("Enter 'q' to quit")
        self.input = str(raw_input("Input: ")) if python_version < 3 else str(input("Input: "))
        print_('-'*20)
    
    def print_exit_message(self):
        print_("Exiting...")
        print_("Thanks for playing.")

    def display_index(self):
        text = """
        1. Reasoning

        """

        for r_key in ReasoningQuestions.index:
            text += "\t{}. {}\n".format(r_keys, ReasoningQuestions.index[r_key]["name"])

        text += "2. Maths\n"
        
        for m_key in MathQuestions.index:
            text += "\t{}. {}\n".format(r_keys, MathQuestions.index[m_key]["name"])

        print_(text)
    
    def display_menu(self):
        level = self.level

        # l = self.levels[self.level][self.input]()
    
    def start_reasoning(self):
        print_("Reasoning")

    def start_maths(self):
        print_("Maths")

    def run(self):
        print_("{} is running".format(self.name))
        print_('-'*20)

        display_menu()
        self.read_input()

        while self.input != "q":

            display_menu()

            self.read_input()
        
        self.print_exit_message()


if __name__ == "__main__":
    app = App()
    app.run()
