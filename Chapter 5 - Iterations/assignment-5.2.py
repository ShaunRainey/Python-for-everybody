# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

largest = None
smallest = None
while True:
    number = input('Input an integer ')
    try:
        if number == 'done':
            break
        if largest is None:
            largest = int(number)
        if smallest is None:
            smallest = int(number)
        if int(number) > largest:
            largest = int(number)
        if int(number) < smallest:
            smallest = int(number)
    except:
        print('Invalid input')
print('Maximum is', largest)
print('Minimum is', smallest)