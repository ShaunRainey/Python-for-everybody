def computeGrade(score):
    if score < 0.0 or score > 1.0:
        print('Invalid score')
        quit()
    elif score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    elif score < 0.6:
        grade = "F"
    return grade

score = input('Enter score: ')

try:
    fscore = float(score)
except:
    print('Error, please enter numeric input')
    quit()

print(computeGrade(fscore))
