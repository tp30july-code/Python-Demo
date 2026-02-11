string1 = input("Enter a palandrom : ")

if(string1 == string1[::-1]):
    print("The string is a palindrom")
else:
    print("the string is not a palindrom")