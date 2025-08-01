# Conditional statements in Python: if, elif, else

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Truthy and Falsy values
# Falsy: False, None, 0, "", [], {}, set(), etc.
value = ""

if value:
    print("Value is not empty")
else:
    print("Value is empty")
