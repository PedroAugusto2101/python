"""
Basic string interpolation
s - string
d and i - int
f - float
x and X - Hexadecimal (ABCDEF0123456789)
"""
name = 'Pedro'
price = 1000.95897643
variable = '%s, the price is $%.2f' % (name, price)
print(variable)
print('The hexadecimal of %d is %08X' % (1500, 1500))

"""
Basic string formatting
s - string
d - int
f - float
.<number of digits>f
x or X - Hexadecimal
(Character)(><^)(amount)
> - Right align
< - Left align
^ - Center align
= - Forces the sign to appear before the zeros
Sign - + or -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}')
print(f'{variable: <10}.')
print(f'{variable: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'The hexadecimal of 1500 is {1500:08X}')
print(f'{variable!r}')

"""
String slicing
 012345678
 Hello world
-987654321
Slicing [i:f:p] [::]
Note: the len function returns the number 
of characters in the string
"""
variable = 'Hello world'
print(variable[::-1])
