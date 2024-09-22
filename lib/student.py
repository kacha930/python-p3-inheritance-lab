#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):

        super().__init__(first_name, last_name)
        self.knowledge = []
    def learn(self, new_string):
        self.knowledge.append(new_string)


    def main():
        student = Student("John", "Doe")
        student.learn("Python is awesome")
        student.learn("code is awesome")
        print(student.knowledge)


    if __name__ == "__main__":
        main()