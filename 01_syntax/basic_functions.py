# basic_functions.py
# Demonstration of basic built-in Python functions
# These functions are fundamental and frequently used in day-to-day programming.

# --- print(): outputs text or variables to the console
print("Hello, world!")  # Output: Hello, world!

name = "Alice"
print("My name is", name)  # Output: My name is Alice

# --- input(): receives user input from the keyboard
# Note: input() returns a string
# user_name = input("What is your name? ")  # Example: If input is "John", user_name will be "John"
# print("Nice to meet you,", user_name)

# --- len(): returns the length of a string, list, tuple, etc.
text = "Python"
print(len(text))  # Output: 6

my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4

# --- type(): shows the data type of a variable
number = 42
print(type(number))  # Output: <class 'int'>

pi = 3.14
print(type(pi))  # Output: <class 'float'>

# --- str(), int(), float(): convert between data types
num_str = "123"
num_int = int(num_str)
print(num_int + 1)  # Output: 124

real_num = 3.5
str_num = str(real_num)
print("The number is " + str_num)  # Output: The number is 3.5

# --- round(): rounds a float to a given number of decimal places
print(round(3.14159, 2))  # Output: 3.14

# --- max() and min(): return the largest/smallest element in an iterable
values = [5, 8, 2, 10]
print(max(values))  # Output: 10
print(min(values))  # Output: 2

# --- sum(): returns the total sum of elements in an iterable
print(sum(values))  # Output: 25

# --- abs(): returns the absolute value of a number
print(abs(-7))  # Output: 7

# --- help(): shows documentation for a function or object
# help(print)  # Uncomment this line to see documentation in the console
