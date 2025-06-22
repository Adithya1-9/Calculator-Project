def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y!=0:
        return x/y
    else:
        return "Cannot divide by zero"
def mod(x,y):
    return x%y
def power(x,y):
    return x**y
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
print("6. Power")

choice=input("Enter choice (1,2,3,4,5,6): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice=='1':
    print("Result:",add(num1,num2))
elif choice == '2':
    print("Result:", sub(num1, num2))
elif choice == '3':
    print("Result:", mul(num1, num2))
elif choice == '4':
    print("Result:", div(num1, num2))
elif choice == '5':
    print("Result:", mod(num1, num2))
elif choice == '6':
    print("Result:", power(num1, num2))
else:
    print("Invalid input")
