'''
Question:
Write a Python program to create a person class. Include attributes like name, country and date of birth. 
Implement a method to determine the person's age.

https://w3resource.com/python-exercises/oop/python-oop-exercise-2.php
'''
from datetime import datetime,date

class Person:
    def __init__(self,name,country,dob):
        print("Creating Person Object For :",name)
        self.name =name
        self.country=country
        self.dob=dob
    
    def show_person_details(self):
        print("Showing Person Details Of :",self.name)
        print("Name   :",self.name)
        print("Country:",self.country)
        print("DOB    :",self.dob)

"""
    def calculate_age(self):
        # # datetime.strptime('2011-03-07','%Y-%m-%d')
        # datetime.strptime(self.dob,'%Y-%m-%d')
        
        # print("Todays Date :",datetime.utcnow())
        # return abs((datetime.utcnow() - datetime.strptime(self.dob,'%Y-%m-%d')).year)
        print(f"Age Of {self.name} is:")
        # return abs((datetime.date.today()-datetime.strptime(self.dob,'%Y-%m-%d')).days)
        return datetime.strptime(self.dob,'%Y-%m-%d')-datetime.date.today()
"""


if __name__ =='__main__':
    p1 =Person('Stopper','Aus','1990-01-01')
    p1.show_person_details()
    p1.calculate_age()