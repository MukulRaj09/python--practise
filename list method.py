# list = [i*i for i in range(8)]
# print(list)
# lst = [i*i for i in range(8) if i%2 == 0]
# print(lst)
# lst.append(7) #add in list
# print(lst)
# #lst.sort() #for in sort or in same order 

# #lst.sort(reverse=True) #reverse in order
# #lst.reverse() #reverse the lst but not in order
# #print(lst)

# print(lst.index(7))
# if lst.index in lst:
#     print("yes")
# else:
#     print("no") #this will find some int on which place.
# print(lst.count(7)) # this will count the int how many times repeat.
l= [5,7,9,"g",8,9,0,]
m = l.copy()
l.insert(1, 34) #insert new term  in list at certain position
print(l)
n = [3,5,6]
l.extend(n) # add new list in other list
print(l)