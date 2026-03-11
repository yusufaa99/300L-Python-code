import sys

print("Welcome to Grading System\n")

# exception handling method to handle invalid user input, it only accepts
# integer(whole numbers) and float (decimal numbers).
def exception_handling(value):

    while True:
        value = input('Enter a number :')

        try:
            num = float(value)
            if '.' in value:
                return num
            elif num > 100:
                print("Scores can not be more than 100")
            # elif score < 0:
            #     print("Scores can not be less than 0")
            else:
                return  num
        except ValueError:
            if value == "quit()":
                return quit()
            else:
                print('invalid input')
    print(counter)

def grading(inputs):

    score = float(inputs)
    # if score > 100:
    #     print("Scores can not be more than 100")
    # # elif score < 0:
    # #     print("Scores can not be less than 0")
    # else:
    if score >= 70:
          print(f"{score}: A")
    elif score >= 60:
        print(f"{score}: B")
    elif score >= 50:
        print(f"{score}: C")
    elif score >= 40:
        print(f"{score}: D")
    elif score >= 35:
        print(f"{score}: E")
    else:
        print(f"{score}: F")

def quit():
    print("Bye")
    return sys.exit(0)
# quit()
inputs = exception_handling(0.0)
grading(inputs)





# inputs = input("Enter Score :\n")
#
# #print(inputs, inputs.isdigit())
# if not inputs.isdigit():
#     print("inValid input")
# else:
#     score = int(inputs)
#     if score > 100:
#         print("Scores can not be more than 100")
#     # elif score < 0:
#     #     print("Scores can not be less than 0")
#     else:
#         if score >= 70:
#             print("A")
#         elif score >= 60:
#             print("B")
#         elif score >= 50:
#             print("C")
#         elif score >= 40:
#             print("D")
#         elif score >= 35:
#             print("E")
#         else:
#             print("F")
#

# print(isfloat(0.0))