# def average(a=9,b=1):
#     print("The average of ",a," and ",b," is ",(a+b)/2) 

# average(4,5)
# average(2)
# average()

def name(fname,mname="John",lname="Doe"):
    print(fname,mname,lname)
    
# name("Shashank")

def average(*numbers):
    print(type(numbers))
    sum = 0
    for number in numbers:
        sum = sum + number
    print("The average of ",numbers," is ",sum/len(numbers))
    

# average(4,5) # this argument will go as a tuple



def name(**names):
    print(type(names))
    print("Hello ",names["fname"],names["mname"],names["lname"])

# name(mname="Rohan",lname="Doe",fname="Shashank")





def average2(*numbers):
    print(type(numbers))
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum/len(numbers)

print(average2(4,5))