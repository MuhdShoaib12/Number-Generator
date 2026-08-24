# Project 1 - NUMBER TABLE GENERATOR

def add_table(start,stop,operand):
    for num in range(start,stop + 1):
        print(f"{num} + {operand} = {num + operand}")
    print()

def sub_table(start,stop,operand):
    for num in range(start,stop + 1):
        print(f"{num} - {operand} = {num - operand}")
    print()    
    
def multi_table(start,stop,operand):
    for num in range(start,stop + 1):
        print(f"{num} * {operand} = {num * operand}")
    print()


def div_table(start,stop,operand):
    for num in range(start,stop + 1):
        if operand == 0:
            print("Undefine. Cannot divide by zero....")
        print(f"{num} / {operand} = {num / operand}")
    print()

def square_table(start,stop):
    for num in range(start,stop + 1):
        print(f"{num}2 = {num ** 2}")
    print()   

def square_root_table(start,stop):
    for num in range(start,stop + 1):
        print(f"sqr {num} = {num ** 0.5}")
    print()   

def cube_table(start,stop):
    for num in range(start,stop + 1):
        print(f"{num}3 = {num ** 3}")
    print()   

def cube_root_table(start,stop):
    for num in range(start,stop + 1):
        print(f"{num}2 = {num ** (1/3)}")
    print()   
print("Number Table Generator")
start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))
operand = 1
while True:     
    print("MENU")
    print("1. Addition Table")
    print("2. Subtraction Table")
    print("3. Multiplication Table")
    print("4. Division Table")
    print("5. Square Table")
    print("6. Square Root Table")
    print("7. Cube Table")
    print("8. Cube Root Table")
    print("9. Exit")
    print()

    choice = int(input("Enter your choice: "))
    if choice in [1,2,3,4]:
        operand = int(input("Enter the operand: "))

    if choice == 1:
      add_table(start,stop,operand)
    elif choice == 2:
        sub_table(start,stop,operand)
    elif choice == 3:
        multi_table(start,stop,operand)
    elif choice == 4:
        div_table(start,stop,operand) 
    elif choice == 5:
        square_table(start,stop)
    elif choice == 6:
      square_root_table(start,stop)
    elif choice == 7:
        cube_table(start,stop) 
    elif choice == 8:
        cube_root_table(start,stop)     
    elif choice == 9:
        print("Exiting the program.")
        break
    else:
        print("Invalid Choice. Please try again.....")        

