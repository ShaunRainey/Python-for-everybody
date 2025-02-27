#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input('Enter score: ')

try:
    fscore = float(score)
except:
    print('Error, please enter numeric input')
    quit()

if fscore < 0.0 or fscore > 1.0:
    print('Invalid score')
    quit()
elif fscore >= 0.9:
    grade = "A"
elif fscore >= 0.8:
    grade = "B"
elif fscore >= 0.7:
    grade = "C"
elif fscore >= 0.6:
    grade = "D"
elif fscore < 0.6:
    grade = "F"
print(grade)