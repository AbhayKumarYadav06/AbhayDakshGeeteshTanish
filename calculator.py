print("we are making a calculator.")
print("this is only for git practice of branching and PR request.")

def add(a,b):
    return a+b

def floor(a):
    return floor(a)

def divide(a, b):
    if(b == 0):
        print("Error!")
        return 0
    else:
        return a / b
    



# ========================
# BASIC OPERATIONS
# ========================



def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def floor_div(a, b):
    if b == 0:
        print("Error! Division by zero")
        return 0
    return a // b


# ========================
# MENU
# ========================

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Modulus")
print("7. Floor Division")

choice = int(input("\nEnter Choice: "))

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if choice == 1:
    print(add(a, b))

elif choice == 2:
    print(subtract(a, b))

elif choice == 3:
    print(multiply(a, b))

elif choice == 4:
    print(divide(a, b))

elif choice == 5:
    print(power(a, b))

elif choice == 6:
    print(modulus(a, b))

elif choice == 7:
    print(floor_div(a, b))

else:
    print("Invalid Choice")
