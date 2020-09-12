import re
file = open('actual.txt', 'r')
sum = 0
for line in file:
    numbers = re.findall('[0-9]+', line)
    for i in numbers:
        sum = sum + int(number)
print(sum)
