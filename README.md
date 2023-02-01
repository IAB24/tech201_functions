# tech201_functions

# Functions

D R Y

Don't  repeat yourself

## Create a function
```` python

 def print_something():
     print("Something has been printed")

 print_something()
````


## Functions and arguments


public void print_string(String_text)

 naming your arguments properly is critical

```` python 
def greetings(name):
     print("Hello, my name is " + name)

 greetings("Ilyas")
 greetings("Belal")
 
````


## The Return statement

````python
def addition(int1, int2):
     return int1 + int2

 print(addition(2,2))


 Default arguments
 def addition(int1=2, int2=2):
     return int1 + int2

 print(addition())
 print(addition(10,10))
````

## Multiple arguments

```` python
 def multi_args(*multiargs):
     print(type(multiargs))

     for arg in multiargs:
         print(arg)
 multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
````

## Type Hints

````python
 def greeting(name: int):
     print("Hello, my name is " + name)

 greeting(24601)

 def division(num1: int = 5, num2: int = 2) -> float:
     return num1 / num2
 print(division())
 ````


## Function best practices

- Name your functions using lower case and underscores
- All arguments should be clear in their need and where possible include their expected type
- Remember return statements or your functions will return None
- Keep functions small to preserve readability and simplicity
- Use comments in your functions/methods to give instructions on how to use them
- Consider using type hints to avoid type errors when you run your code.