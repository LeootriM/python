from pyexpat.errors import messages

total = 0

for number in range(1,11):
    if number %2 == 0:
        total +=number
print("shuma e numrave qift pre 1 deri ne 10 eshte: " ,total)


def greet():
    print("hello world")

greet()

def greet_person(name):
    print("hello" , name)

greet_person("filan")

greeting = "hello"

def greet(name):
    message = f"{greeting} , {name}!"
    print(message)

greet("michael")
print(greeting)


def greet_person(name, greeting="hello"):
    message = f"{greeting} , {name}!"
    return message

default_greeting = greet_person("rijan")
custom_greeting = greet_person("eris" , "Hi")
print(default_greeting)
print(custom_greeting)





