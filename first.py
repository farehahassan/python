fname = input("First name: ");
lname = input("Last name: ");

age = input("Your age: ");
print(fname + lname + age );       

#this does not giving error because compiler consider this age variable as string but if we remove input from here then it'll give the concatenate str error which can be resolve by using TYPE CONVERSION

#Type Conversion 

age = int(input("Your age"));
print(age); 

# same as for float() str() boo()

#Adding two numbers

first = int(input("enter first numbers : "));
second = int (input("enter second number : "));
sum = first + second;
print("The sum is : " +str( sum))
