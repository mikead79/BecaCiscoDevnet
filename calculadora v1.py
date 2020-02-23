# Calculadora with on console menu operations
import math

def suma():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} + {num2} = {num1+num2}")

def resta():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} - {num2} = {num1-num2}")

def multiplica():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} * {num2} = {num1*num2}")

def divide():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} / {num2} = {num1/num2}")

def potencia():
    num1 = float(input("The number: "))
    num2 = float(input("The power to raise at: "))
    print(f"{num1} ** {num2} = {num1**num2}")

def raiz():
    num = float(input("The number to extract the square root from: "))
    print(f"The square root of {num} = {math.sqrt(num)}")

print("""1 Addition
2 Substraction
3 Multiplication
4 Division
5 Raise to power
6 Square root""")
while True:
    op = input("Choose an operation (by entering his number or 0 to exit): ")
    if op == '1':
        suma()
    elif op == '2':
        resta()
    elif op == '3':
        multiplica()
    elif op == '4':
        divide()
    elif op == '5':
        potencia()
    elif op == '6':
        raiz()
    elif op == '0':
        break
