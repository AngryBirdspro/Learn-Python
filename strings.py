#prints 'word' with all capital letters
word = "tom jia"
print(word.upper())

#prints 'word' with all lowercase letters
word = "tom jia"
print(word.lower())

#checks if 'word' is all capital letters
word = "tom jia"
print(word.upper().isupper())

#checks if 'word' is all lowercase letters
word = "tom jia"
print(word.lower().islower())

#prints index value of 'word'
word = "tom jia"
print(len(word))

#prints assigned index of 'word'
word = "tom jia"
print(word[0])

#prints index value of a letter 'word'
word = "tom jia"
print(word.index("t"))

#replaces index value with another index value in 'word'
word = "tom jia"
print(word.replace("tom", "keon"))