import re

handle = open('actual-data.txt')
numberList = list()

for line in handle:
    list = re.findall('[0-9]+',line)
    if len(list) != 0:
        for number in list:
            numberList.append(float(number))

total = sum(numberList)
length = len(numberList)
print(total)
print(length)
print('Average:', round(total/length))