# Exercise 1: Write a program which repeatedly reads integers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# integers. If the user enters anything other than a integers, detect their mistake
# using try and except and print an error message and skip to the next integers.

total = 0
count = 0
while True:
    integer = input('Input an integer: ')
    try:
        if integer == 'done':
            print('Total:',total)
            print('Number of integers:',count)
            print('Average:', total/count)
            break
        else:
            total = total + float(integer)
            count = count + 1
            continue
    except:
        print('Invalid input, please enter a number')