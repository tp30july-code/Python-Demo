# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The divide is {a / b}")

#     except ValueError:
#         print("Please do not perform invalid calculation")

#     except ZeroDivisionError:
#         print("Hey, do not divide by 0")
        
#     except Exception as e:
#         print("Unknown error occurred!", e)

     
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b==0:
    raise ValueError("Plese dont divide by 0")

print(f"The divide is {a / b}")

 