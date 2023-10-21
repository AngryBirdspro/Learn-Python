def add_numbers():
   num_1 = float(input('Enter first number: '))
   num_2 = float(input('Enter second number: '))
   print('Result = ' + str(num_1 + num_2))
 
def square_number():
   num = float(input('Enter a number: '))
   print(str(num) + ' squared = ' + str(num * num))

def minus_numbers():
    num_1 = float(input('Enter first number: '))
    num_2 = float(input('Enter second number: '))
    print('Result = ' + str(num_1 - num_2))

def multiply_numbers():
    num_1 = float(input('Enter first number: '))
    num_2 = float(input('Enter second number: '))
    print('Result = ' + str(num_1 * num_2))

def divide_numbers():
    num_1 = float(input('Enter first number: '))
    num_2 = float(input('Enter second number: '))
    print('Result = ' + str(num_1 / num_2))

def display():
    print('============')
    print('Main Menu')
    print('1. Add two numbers')
    print('2. Square a number')
    print('3. Minus two numbers')
    print('4. Multiply two numbers')
    print('5. Divide two numbers')
    print('6. Quit')
 
def quit_message():
   print('Goodbye!')
choice = 0
while True:
    display()
    choice = int(input("wat do u chose: "))
    if choice == 1:
        add_numbers()
        display()
    elif choice == 2:
        square_number()
        display()
    elif choice == 3:
        minus_numbers()
        display()
    elif choice == 4:
        multiply_numbers()
        display()
    elif choice == 5:
        divide_numbers()
        display()
    elif choice == 6:
        quit_message()
        break
    else:
        print("read the darn options carefully plz")
        continue