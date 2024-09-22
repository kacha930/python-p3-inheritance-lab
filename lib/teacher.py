#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        
        if knowledge is None:
            self.knowledge = [
                "str is a data type in Python",
                "programming is hard, but it's worth it",
                "javascript async web request",
                "python function call definition",
                "object-oriented teacher instance",
                "programming computers hacking learning terminal",
                "pipenv install pipenv shell",
                "pytest -x flag to fail fast",
            ]
        else:
            self.knowledge = knowledge

    def teach(self):
        return random.choice(self.knowledge)

# Example usage
if __name__ == "__main__":
    teacher = Teacher("John", "Doe")
    print(f"{teacher.first_name} {teacher.last_name} teaches: {teacher.teach()}")

