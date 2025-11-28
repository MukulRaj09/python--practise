# marks = [3, 0, 6, "9", True , 8, 8 ,99 ,9]

# print(marks)
# print(type(marks))
# print(marks[0])  #ordered data of collection data 
# print(marks[3])

# print(type(marks[3]))   #numering of list starts from 0

# print(marks[-3])  #negative index
# print(marks[len(marks)-3])  #positive index

# print(marks[5-3])  #positive index

# print(marks[2])  #ppositiove index

# if "9" in marks:  #find from list
#     print("yes")

# else:
#     print("no")

# if "ju" in "jujutsui":  #same for str

#     print("yes")
# print(marks[1:4]) #slicing of list
# print(marks[1: 4: 2])  #jumping in that sliced list


lst = [i*i for i in range(8)]
print(lst)
lst = [i*i for i in range(8) if i%2 == 0]
print(lst)