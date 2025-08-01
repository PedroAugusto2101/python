# FOR loop over a list
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

# WHILE loop with condition
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Loop with break and continue
for i in range(5):
    if i == 3:
        continue  # Skip 3
    if i == 4:
        break     # Stop at 4
    print(i)
