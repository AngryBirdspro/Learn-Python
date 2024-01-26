numbers = [4, 3, 1, 2,]
friends = ['tom', 'keon', 'jethro', 'sammuel']
print(friends)

#prints everything after and including index 1
print(friends[1:])

#prints everything up to excluding index 3
print(friends[1:3])

#adds that into friends
friends.append('aneesh')
print(friends)

#removes item in the last index value
friends.pop()
print(friends)

#adds that into friends at designated index
friends.insert(1, 'aneesh')
print(friends)

#prints the items in alphabetical order
friends.sort()
print(friends)

#prints numbers in ascending order
numbers.sort()
print(numbers)

#combines friends w/ numbers
friends.extend(numbers)
print(friends)

#copies and prints friends
friend = friends.copy()
print(friend)

#prints index value of the item
print(friends.index('tom'))

#prints the frequency of presence of the item
print(friends.count('tom'))

#empties list
friends.clear()
print(friends)

# test