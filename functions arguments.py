# def average(a=1,b=7):  # a,b are required arguments
#     print("tthe average is ",(a+b)/2)

# #average(4,5)

# average()  #default value
# average(3,6)  #its ignore the date given in function
# average(4)  #is takes defaule value 

# #required arguments where you must put the value atleat one.
# def average(a, b, c=4):
#     print("average: ",(a+b+c)/3)
# average(3, 6)  #here value of c is taken as defaut

def average(*numbers):   #this * use as arbitrary arguments work as touple
#    print(type(numbers))
    sum = 0
    for i in  numbers:
        sum = sum +i

#     print("average is :",sum/len(numbers))
    return sum/len(numbers)  #return means take value and show direct value
# average(5, 7, 0, 3 ,6)
c = average(5, 7, 0, 3 ,6)
print(c)

# def name(**name):  #name as dictonary
#     print(type(name))
#     print("hellow,",name["fname"],
# name["mname"],name["lname"])
    
# name(mname="hieri", lname="uifhi",fname="uhrei")