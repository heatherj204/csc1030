#!/usr/bin/env python3

class Test():
    def __init__(self, subjuct_name, correct_answers, passing_mark) -> None:
        self.subjuct_name = subjuct_name
        self.correct_answers = correct_answers
        self.passing_mark = int(passing_mark.strip('%'))

class Student():
    def __init__(self, name) -> None:
        self.name = name

    def take_test(self, test: Test, answers):
        correct = []
        for answer in answers:
            if answer in test.correct_answers:
                correct.append(answer)

        grade = (len(correct) / len(test.correct_answers)) * 100

        if grade <= test.passing_mark:
            print(f"{self.name} faild the {test.subjuct_name} test!")
        else:
            print(f"{self.name} passed the {test.subjuct_name} test with the score {grade}%")

paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

stu1 = Student('Tom')
stu1.take_test(paper2, ['1C', '2C', '3D', '4A'])

stu2 = Student('John')
stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B'])
