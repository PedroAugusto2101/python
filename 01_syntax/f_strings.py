name = 'Pedro Augusto'
height = 1.75
weight = 80
bmi = weight / height ** 2

# f-strings
line_1 = f'{name} is {height:.2f} meters tall,'
line_2 = f'weighs {weight} kilograms and his BMI is'
line_3 = f'{bmi:.2f}'

print(line_1)
print(line_2)
print(line_3)

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={name2} a={name1} a={name1} c={name3:.2f}'
formatted = string.format(
    name1=a, name2=b, name3=c
)

print(formatted)
