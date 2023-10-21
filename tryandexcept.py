try:
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError:
    print('read the instructions dumbass')
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('read the instructions dumbass')