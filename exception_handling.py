import sys
counter = 0
def isfloat(value):
    while True:
        value = input('Enter a number :')
        try:
            num = float(value)
            if '.' in value:
                return num
            else:
                return  num
        except ValueError:
            if value == "/c":
                return "bye"
            else:
                print('invalid input')

def grading(inputs):
    # inputs = input("Enter Score :\n")

    score = float(inputs)
    if score > 100:
        print("Scores can not be more than 100")
    # elif score < 0:
    #     print("Scores can not be less than 0")
    else:
        if score >= 70:
            print("A")
        elif score >= 60:
            print("B")
        elif score >= 50:
            print("C")
        elif score >= 40:
            print("D")
        elif score >= 35:
            print("E")
        else:
            print("F")

inputs = isfloat(0.0)
grading(inputs)
# print(isfloat(0.0))

