#TASK1: Writing Functions

def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(a, b):
    return a + b

# Usage Output
greet_user("Alice")
result = add_numbers (5, 10)
print(f"The sum of 5 and 10 is {result}.")

#TASK2:Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Usage
describe_pet("Buddy")              # Default is dog
describe_pet("Whiskers", "cat")    # Override default

#TASKS3: Functions with variable argument
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# Usage
make_sandwich("Lettuce", "Tomato", "Cheese")

#TASK4: Understanding Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#  Usage
print(f"Factorial of 5 is {factorial(5)}.")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")

