first_num = int(input("What is your first number?: "))
print("+ - * /")
operator = input("Pick an operator: ")
next_number = int(input("What is your next number?: "))

def calc(num1, num2, op):
    """This function takes two numbers to calculate along with an operator symbol. It returns the calculated amount."""
    result = 0
    if op == "+":
        print(f'{num1} + {num2} = {num1+num2}')
        result = num1 + num2
    if op == "-":
        print(f'{num1} - {num2} = {num1-num2}')
        result = num1 - num2
    if op == "*":
        print(f'{num1} * {num2} = {num1*num2}')
        result = num1 * num2
    if op == "/":
        print(f'{num1} / {num2} = {num1/num2}')
        result = num1 / num2

    again = input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation: ')

    if again.lower() == "y":
        operator = input("Pick an operator: ")
        next_number = int(input("What is your next number?: "))
        result = calc(result, next_number, operator)
        
    if again.lower() == "n":
        print(result)
        return result

result = calc(first_num, next_number, operator)