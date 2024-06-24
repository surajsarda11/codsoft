number1=float(input("enter the first number"))
number2=float(input("enter the second number"))
operator=input("enter the operator('+','-','*','/','%')")
if operator=="+":
    try:
       sum= number1+number2
    except Exception :
        print("sum:",sum)
elif operator=="-":
    print("subtraction:",number1-number2)
elif operator=="*" or "X" or "x":
    print("multiplication",number1*number2)
elif operator=="/":
    print("division:",number1/number2)
elif operator=="%":
    print("Remainder:",number1%number2)
else:
    print("operator invalid")