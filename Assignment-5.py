def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")
    # question(2a)
    subject=["Americans","Indians"]
verb=["play","watch"]
objects=["Baseball","Cricket"]

# List Comprehension
Syntax = [(Sub+' '+vrb+' '+Objct+".") for Sub in subject for vrb in verb for Objct in objects]

#for Loop for Iteration
print("Output:")

for syn in Syntax:    
    print(syn)