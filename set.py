s1= {2, 4, 3 ,2 ,5 ,6.7 ,8 , "red" }  # set don't consider same value twice
s2 = {3,6,8,9}
print(s1) # use {} in set
# no order maintaion
# set are imutable .

mukul = {"mukul" } # empty braces are concider as dict not set
print(type(mukul))


mukul = set() #then it's set and no use of curley bracket

for value in s1:
    print(value)


s1.update(s2)  # they will give new set including both.
print(s1.union(s2))


# s3 =s1.itersection(s2)  # which in both set.


s3=  s1.isdisjoint(s2)
print(s3)

    