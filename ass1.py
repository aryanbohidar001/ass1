a=input("Enter the first number :")
b=input("Enter the second number :")
a=int(a)
b=int(b)

sum=a+b
sub=a-b
multi=a*b
div=a/b


print("Addition: ",sum)
print("Subtraction: ",sub)
print("Multiplication: ",multi)
if(b==0):
    print("Division by zero is not allowed")
else:
    print("Division: ",div)