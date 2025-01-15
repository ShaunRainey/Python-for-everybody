num = "444444444444444444444444444444444444"

count = 0
i = 0
while i < len(num):
    if num[i] == "4":
        count += 1
        i +=1

print(count)