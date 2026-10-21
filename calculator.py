print("====calculator====")
print("1.sum")
print("2.subtraction")
print("3.zarb")
print("4.taqsim")
print("5.tavan")
num1=float(input("enter the first number:"))
operator=input("select an operation")
num2=float(input("enter the second number:"))
if operator=="+":
    print("natijeh=",num1+num2)
elif operator=="_":
    print("natijeh=",num1-num2)
elif operator=="*":
    print("natijeh=",num1*num2)
elif operator=="/":
    if num2!=0:
     print("natijeh=",num1/num2)
    else:
     print("taqsim bar sefr emkan pazir nist!!!")
elif operator=="**":
     print("natijeh=",num1**num2)
else:
     print("the operation is invalid")