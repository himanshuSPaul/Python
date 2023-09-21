''''
https://w3resource.com/python-exercises/oop/python-oop-exercise-1.php
Question
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

'''


class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14159265*self.radius*self.radius
    
    def calculate_perimeter(self):
        return  2*3.14159265*self.radius
    
    def calculate_diameter(self):
        return 2*self.radius




if __name__ =='__main__':

    circle1 = Circle(10)
    print("Radius Of Circle Is :",circle1.radius)
    print("Diameter Of Circle Is :",circle1.calculate_diameter())
    print("Perimeter Of Circle :",circle1.calculate_perimeter())
    print("Perimeter Of Circle :",circle1.calculate_area())


