import sys
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def mod(a, b):
    return a % b

def power(a, b):
    return a ** b
operation = str(sys.argv[1])
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

# print(add(10, 5))
# print(sub(10, 5))
# print(mul(10, 5))
# print(div(10, 5))
# print(mod(10, 5))
# print(power(10, 5))
if operation == 'add':
    out = add(num1, num2)
    print(out)