#r stands for read, w stands write which can alllow changes, a stands for append, r+ mean read and write
file = open("name.txt", "r")
print(file.readable())
file.close()