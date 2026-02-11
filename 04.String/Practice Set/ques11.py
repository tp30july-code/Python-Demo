sentence = "Coding in Python is fun"
sum = 0 
vowals = ['a', 'e' , 'i' , 'o' , 'u']

for char in sentence:
    if(char in vowals):
        sum += 1

print(f"There are {sum} vowals in this sentence")