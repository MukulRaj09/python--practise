def meanvalue(a, f):
    mean=(a*f)/(a+f)
    print("meanvalue:",mean)

def isgreater(a,f):
    if(a>f):
        print("first is greater")
    else:
        print("secound is greater or equal")

def inlesser(a,f):
    pass

a=45
f=67
isgreater(a,f)
meanvalue(a,f)  # by naming function,this is a way to call function 

b=8
g=7
isgreater(b,g)
meanvalue(b,g)