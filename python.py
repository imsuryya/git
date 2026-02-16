# Python Demo Script
# Added on v3 branch

def greet(name):
    """Function to greet a user"""
    return f"Hello, {name}! Welcome to Git learning."

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

def subtract_numbers(a, b):
    """Function to subtract two numbers - added on main by another user"""
    return a - b

def multiply_numbers(a, b):
    """Function to multiply two numbers - added in feature branch"""
    return a * b

if __name__ == "__main__":
    print(greet("Developer"))
    print(f"Sum of 5 and 3 is: {add_numbers(5, 3)}")
