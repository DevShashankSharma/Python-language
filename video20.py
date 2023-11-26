# a = 9
# b = 8
# gmean1 = (a*b)/(a+b)
# print(gmean1)

# c = 8
# d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)

def calculateGmean(a,b): 
    gmean = (a*b)/(a+b)
    print(gmean)

def isGreater(a,b):
    if(a>b):
        print("a is greater than b")
    elif(b>a):
        print("b is greater than a")
    else:
        print("a and b are equal")

calculateGmean(8,7)
calculateGmean(9,8)


def isLesser(a,b):
    pass       # When we have to write code later on we use pass keyword to avoid error in code 