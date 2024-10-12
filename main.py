import random
import math
from utils import *
from reasoning import *
from mathematics import *


class App:
    def __init__(self):
        self.name = "App"
        self.input = ""
        self._game_loop = False
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
                "class": ReasoningQuestions(),
                "items": ReasoningQuestions.index,
            },
            "2": {
                "name": "Maths",
                "class": MathQuestions(),
                "items": MathQuestions.index,
            }
        }

        self.level = 0
        self.current_item = None
        self.current_questions = []

    def read_input(self):
        print('-'*20)

        if self._game_loop:
            print("Enter 'qq' to go back to {} menu".format(self.levels["{}".format(self.level)]["name"]))
            print("Enter 'a' to display answer and a new question.")
        else:
            print("Enter 'q' to quit")
            if self.level != 0:
                print("Enter '00' to go to Main Menu")

        self.input = str(raw_input("Input: ")) if python_version < 3 else str(input("Input: "))
        print('-'*20)
    
    
    def input_processor(self):
        inp = self.input
        level = self.level
        current_item = self.current_item

        c_level = self.levels["{}".format(level)]
            
        if inp not in c_level["items"]:
            print("Invalid input")
            return
            
        self.current_item = inp
        current_item = inp
        
        if level == 0:

            obj = c_level["class"]
            method = c_level["items"][current_item]["method"]

            return getattr(obj, method)()
        else:
            self.game_loop()
        
    
    def game_loop(self):
        self._game_loop = True

        inp = self.input
        level = self.level
        current_item = self.current_item

        c_level = self.levels["{}".format(level)]

        obj = c_level["class"]

        while inp != "qq":

            if inp == "a":
                print("Answer: {}".format(self.current_questions[-1][-1]))

            self.current_questions.append(obj.generate_question(int(current_item)))
            
            q = self.current_questions
            
            print("Question:\n{}\n".format(q[-1][0]))
            
            for o in q[-1][1]:
                print("{}".format(o))
            
            self.read_input()
            inp = self.input
        
        self._game_loop = False

    def run(self):
        print("{} is running".format(self.name))
        print('-'*20)

        self.display_menu()
        self.read_input()

        while self.input != "q":

            if self.input != "00":
                self.input_processor()
            else:
                self.level = 0
                self.current_item = None

            self.display_menu()

            self.read_input()
        
        self.print_exit_message()
    
    def display_index(self):
        text = "-"*5 + "\n"
        text += "Index" + "\n"
        text += "-"*5 + "\n"

        text += "1. Reasoning\n"

        for r_key in ReasoningQuestions.index:
            text += "\t{}. {}\n".format(r_key, ReasoningQuestions.index[r_key]["name"])

        text += "2. Maths\n"
        
        for m_key in MathQuestions.index:
            text += "\t{}. {}\n".format(m_key, MathQuestions.index[m_key]["name"])

        print(text)
    
    def display_menu(self):
        level = self.level

        c_level = self.levels["{}".format(level)]

        print('-'*20)
        print("")
        print(c_level["name"])

        for key in c_level["items"]:
            print("\t{}. {}".format(key, c_level["items"][key]["name"]))
    
    def start_reasoning(self):
        self.level = 1

    def start_maths(self):
        self.level = 2
    
    def print_exit_message(self):
        print("Exiting...")
        print("Thanks for playing.")



if __name__ == "__main__":
    app = App()
    app.run()
