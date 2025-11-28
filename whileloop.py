# i = int(input("enter the number: "))
# while(i<7):
#     print(i)
#     i += 1
# print("done with the loop")

# i = int(input("enter the number: "))
# while(i<=45):
#     print(i)
#     i+=1

i = int(input("enter the number: "))
while(i>=0):
    print(i)   #if you add here the loop will become infinite loop
    i-=1
else:
    print("i am inside else")   #save from infinite loop 