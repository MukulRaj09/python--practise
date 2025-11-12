resume = "hey i am {} and i am from {}"
country ="india"
name = "mukul"
#print(resume.format(name,country))  #value.format for adding 

print(f"hey i am {{name}} and i am from {country}")
price = 45.789
txt = f"for only {price:.2f}dollers"  #you can use double curley braces if you want to keep value as is it.
print(txt)
# print(txt.format(price = 34.990))
print(type(f"{2*34}"))