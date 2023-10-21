print('hello, welcome to the mexican cartel coffee shop')
name = input('name:')
menu = "black coffee, latte, cappucino, espresso, "
if name == "karen" or name == "vegan teacher" or name == "loki":
    vegan = input('r u vegan\n')
    useful = int(input('how useful r u on a scale of 1-10\n'))
    if vegan == 'yes' and useful < 6:
        print('fuck off u good 4 nothing vegan of a ' + name)
        exit()
    else:
        print('well ur still not welcome, here is the menu: ' + menu + 'now hurry up \n' + 'order:')
else:
    print('hi ' + name + ', here is the menu: ' + menu + 'now wat can i get u \n' + 'order:')
orders = input()
number = input('how many cups\n')
if orders == "black coffee":
    price = 13
elif orders == "latte":
    price = 9
elif orders == "cappucino":
    price = 10
elif orders == "espresso":
    price = 4
else:
    print("get ur ears checkt out we dont have that shit here")
    price = 0
    exit()
creamornot = input('do u want whipped cream\n')
if creamornot == "yes":
    print('ok we will add whipped cream to your' + number + ' cups of ' + orders)
    creamprice = 11
    total = price * int(number) + creamprice * int(number)
else:
    total = price * int(number)
print('ok, ' + name + ', the ' + number + ' cups of ' + orders + ' will be ready soon')
print('and that will be $' + str(total))