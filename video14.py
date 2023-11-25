# a = int(input("Enter your age: "))
# print("Your age is :", a)

# print(a>18)
# print(a<18)
# print(a==18)
# print(a!=18)
# print(a>=18)
# print(a<=18)

# if(a>18):
#     print("You can drive")
# else:
#     print("You can't drive")
    
applePrice = 10
budget = 200

if(budget - applePrice > 50):
    print("You can buy 1kg apples")
elif(budget - applePrice > 20):
    print("You can buy 1/2 kg apples")
else:
    print("You can't buy apples")
    

num = 18

if(num<0):
    print("The number is negative")
elif(num>0):
    if(num<=10):
        print("The number is less than 10")
    elif(num<=20):
        print("The number is less than 20")
    else:
        print("The number is greater than 20")
else:
    print("The number is zero")