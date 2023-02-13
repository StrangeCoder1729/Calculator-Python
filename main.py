import calculation
import logo
import os
import input_data
 
print(logo.art)
num1,operation,num2 = input_data.data()
result = calculation.calc(num1,operation,num2)
# print(f"Result : {result}")


while(True):
    again = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start with a new calculation or type 'stop' to quit : ").lower()
    if again == 'y':
        operation,num2 = input_data.data_again(result)
        result =calculation.calc(result,operation,num2)
        # print(f"Result : {result}")
    elif again == 'n':
        os.system('cls')
        result = 0
        num1,operation,num2 = input_data.data()
        result = calculation.calc(num1,operation,num2)
        # print(f"Result : {result}")
    elif again == 'stop':
        print("Thanks for using !!")
        exit()
        # exit()








