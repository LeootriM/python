
class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def calculate_area(self):
      return  self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)




my_Rectangle = Rectangle(4,7)

area = my_Rectangle.calculate_area()

perimeter= my_Rectangle.calculate_perimeter()

print(f"area is: {area}")
print(f"perimeter is {perimeter}")



class Person:
   def __init__(self , name , age):
       self.name = name
       self.age = age

    def greet(self):
        print(f"Hello I am {self.name} amd I am {self.age} years old")


Person1 = Person ("Leotrim" , 17)
Person2 = Person("Arion" ,24)

Person1.greet()
Person2.greet()
