"""
Docstring
Python = Programming language
Typing type = Dynamic / Strong
str -> string -> text
Strings are texts enclosed in quotes
"""
print(1234)

# Single quotes
print('Pedro Augusto')
print(1, 'Pedro "Augusto"')

# Double quotes
print("Pedro Augusto")
print(2, "Pedro 'Augusto'")

# Escape character
print("Pedro \"Augusto\"")

# r -> raw string
print(r"Pedro \"Augusto\"")

# int and float types

# int -> Integer
# The int type represents any positive or negative whole number.
# Unsigned int is considered positive.
# print(11) # int
# print(-11) # int
# print(0)

# float -> Floating-point number
# The float type represents any positive or negative number with a decimal point.
# Unsigned float is considered positive.
# print(1.1, 10.11)
# print(0.0, -1.5)

# The type function shows the type that Python
# inferred for the value.
print(type('Pedro'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

# bool (boolean) data type

# When asking a question in a program,
# there are only two possible answers:
# yes (True) or no (False).
# There are several operators to "ask questions".
# Among them is ==, a logical operator that
# asks if one value is equal to another.
print(10 == 10)  # Yes => True
print(10 == 11)  # No  => False
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# Type conversion, typecasting, coercion
# The act of converting one type into another
# Immutable and primitive types:
# str, int, float, bool - immutable
# Weak typing means the language converts
# one of the values to execute correctly
# Strong typing results in an error because
# it doesn't convert automatically
# Dynamic typing doesn't require declaring the data type
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')
