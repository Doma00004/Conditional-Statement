x=int(input("Enter any number:"))
result="{} is positive"
result2="{} is negative"
if x>=0:
    print(result.format(x))
else:
    print(result2.format(x))
