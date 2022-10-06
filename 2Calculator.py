#Calculator Program
#+ - * / %
print("Press 1: For Add")
print("Press 2: For Subtract")
print("Press 3: For Multiply")
print("Press 4: For Divide")
option = int(input("Please enter something: "))
print(type(option))
firstNumber = int(input("Please enter first number: "))
secondNumber = int(input("Please enter second number: "))
if option == 1:
    totalNumber = firstNumber + secondNumber
elif option == 2:
    totalNumber = firstNumber - secondNumber
elif option == 3:
    totalNumber = firstNumber * secondNumber
elif option == 4:
    totalNumber = firstNumber / secondNumber
else:
    print("You must enter 1/2/3/4: ")
# print("Total Number is: ",totalNumber)
print("The number of {} {} {} is {}".format(firstNumber,option,secondNumber,totalNumber))
#default အနေနဲ့ string အနေနဲ့ဖတ်ပေးတာ
#string '1' not equal int 1
