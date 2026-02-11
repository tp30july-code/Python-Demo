def very_slow_function():
    print("Something......")
    print("Something......")
    print("Something......")
    print("Something......")
    print("Something......")
    return 70

# a = very_slow_function()
# if(a:=very_slow_function()>10):
#     print(a)
# else:
#     print("Its not greater than 10")

while(data:=input("Enter a number: ")):
    print(data)
    if data == "q":
        break