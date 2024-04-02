a=int(input("Enter your number:"))
num="{} does not satisfy any condition."
if a%3==0 and a%5==0:
    print("Fizzbuzz")
elif a%5==0:
    print("Buzz")
elif a%3==0:
    print("Fizz")
else:
    print(num.format(a))
