# tech201_functions

# Functions

D R Y  (Don't  repeat yourself) 
- It is easy to create errors that are hard to spot when writing long blocks of code.
- Have to make changes in numerous places so it is time consuming.
- Instead, you can create functions that perform those tasks, using sets of arguments or inputs to specify how the task is performed.

### Create a function
- In Python a function is defined using the 'def' keyword
- To call a function, use the function name followed by parenthesis:

```` python

 def print_something():
     print("Something has been printed")

 print_something()
 0utput = "Something has been printed"
````

### Functions and arguments
- Information can be passed into functions as arguments.
- Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
- Naming your arguments properly is critical

```` python 
def greetings(name):
     print("Hello, my name is " + name)

 greetings("Ilyas")
 greetings("Belal")
 
````

### The Return statement
- The 'return' statement is used to store data. 
- You can use the return statement to make your functions send Python objects back to the caller code. These objects are known as the function’s return value. 
- Without a return function your output would be 'None'.

````python
def addition(int1, int2):
    return int1 + int2

 print(addition(2,2))
#Output = 4
````
### Default arguments
- These arguments that take default values if no explicit values are passed to these arguments from the function call
````python
def addition(int1=2, int2=2):
     return int1 + int2

 print(addition())
 print(addition(10,10))
````

### Multiple arguments
- Sometimes you may need additional information for the function to run successfully.
- You can write functions that take in more than one parameter by defining as many parameters as needed, for example:
```` python
 def multi_args(*multiargs):
     print(type(multiargs))

     for arg in multiargs:
         print(arg)
 multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
````
- '*' allows you to create a function with multiple arguments and creates a tuple.

### Type Hints
- Function that warns users when arguments with the wrong type of values are being passed.
- The name input should be a string so python returns a type error and highlights this as a hint.
````python
def greeting(name: int):
     print("Hello, my name is " + name)

 greeting(24601)
````
- By defining the datatype you can express the type of output you want as long as the arguments are suitable.
````python
def division(num1: int = 5, num2: int = 2) -> float:
     return num1 / num2
 print(division())
 ````

### Functions best practices

- Name your functions using lower case and underscores
- All arguments should be clear in their need and where possible include their expected type
- Remember return statements or your functions will return None
- Keep functions small to preserve readability and simplicity
- Use comments in your functions/methods to give instructions on how to use them
- Consider using type hints to avoid type errors when you run your code.