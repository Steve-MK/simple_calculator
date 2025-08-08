# simple calcilator 
value1 = float(input("Enter value1: "))
value2 = float(input("Enter value2: "))

#to help identify operations 
operation = input("pick one operation from ' + , - , * , / '  ")

#now for the calculation bit
if operation == '+':
    result = value1 + value2
    print(f" {value1} + {value2} = {result}")
elif operation == '-':
    result = value1 - value2
    print(f" {value1} - {value2} = {result}")
elif operation == '*':
    result = value1 * value2
    print(f" {value1} * {value2} = {result}")
elif operation == '/':
    if value2 != 0:    
        result = value1 / value2
        print(f" {value1} / {value2} = {result}")
    else:print("Error: division by zero not allowed")

else: print("Invalid opperation Please use + , - , * , or /")
