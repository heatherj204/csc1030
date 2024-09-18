#!/usr/bin/env python3

class Test():
    def __init__(self, subjuct_name, correct_answers, passing_mark) -> None:
        self.subjuct_name = subjuct_name
        self.correct_answers = correct_answers
        self.passing_mark = passing_mark
        passing_mark = self.passing_mark.strip('%')
        passing_mark = int(passing_mark)
        print(passing_mark)


paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

class Student():
    def __init__(self, name) -> None:
        self.name = name

    def take_test(self, other, answers):
        self.answers = answers
        correct_answers = other.correct_answers
        if answers == correct_answers:
            return print(f'{self.name} passed the {other.subject_name} test with the score of 100%')
        elif
