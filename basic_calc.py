
first = input("enter first number")
operation = input("enter your operation (+,-,*,/,%)")
second = input("enter second number")

first = int(first)
second = int(second)

if operation == '+':
    print(first + second)
elif operation == '-':
    print(first - second)
elif operation == '*':
    print(first * second)
elif operation == '/':
    print(first / second)
elif operation == '%':
    print(first % second)
else: print ("invalid")     