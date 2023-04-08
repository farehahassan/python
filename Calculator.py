first = int(input("Enter first number : "));
second = int(input("Enter second number : "));

print(" 1) + for addition \n 2) - for multiplication \n 3) * for multiplication \n 4) ** for power \n 5) / for division \n 6) // for division without decimal numbers \n 7) % for remainder")

op = input("Enter operator to perform : ");
sum = first + second;
sub = first - second;
mul = first * second;
dmul = first ** second;
ddiv = first // second;
div = first / second;
rem = first % second;

if op=='+':
    print("The sum is : " + str(sum))
    
elif op =='-':
    print("The subtraction is : "+ str(sub))
    
elif op =='*':
    print("The multiplication is : "+ str(mul))
    
elif op =='/':
    print("The division is : "+ str(div))
    
elif op =='//':
    print("The division without decimal values is : "+ str(ddiv))
    
elif op =='%':
    print("The remainder or modulo is : "+ str(rem))
    
elif op =='**':
    print("The power is : "+ str(dmul))
    
else:
    print("Invalid operator");