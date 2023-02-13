


def calc(num1,operation,num2):

    if operation == '+':
        ans = round(num1 + num2,2)
        print(f"{num1} + {num2} = {ans}")
        return ans
    elif operation == '-':
        ans = round(num1-num2,2)
        print(f"{num1} - {num2} = {ans}")
        return ans
    elif operation == 'x':
        ans = round(num1 * num2,2)
        print(f"{num1} x {num2} = {ans}")
        return ans
    elif operation == '/':
        ans = round(num1 / num2,2)
        print(f"{num1} / {num2} = {ans}")
        return ans
    else:
        print("Used an invalid operation")
        exit()

# def calc2(res,operation,num2):
#     if operation == '+':
#         print(f"{res} + {num2} = {res + num2}")
#         return res + num2
#     elif operation == '-':
#         print(f"{res} - {num2} = {res - num2}")
#         return res - num2
#     elif operation == 'x':
#         print(f"{res} x {num2} = {res * num2}")
#         return res * num2
#     elif operation == '/':
#         print(f"{res} / {num2} = {res / num2}")
#         return round(res / num2,2)
#     else:
#         print("Used an invalid operation")
#         exit()


