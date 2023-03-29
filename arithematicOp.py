first = int(input("enter first num: "));
sec = int(input("enter second num: "));

print (first + sec);        #add
print (first - sec);        #sub
print (first / sec);        #divide
print (first // sec);       # double slash use when we dont want values in decimal 
print (first * sec);        #multiply
print (first **sec);        #** coverts in power
print (first % sec);        #remainder OR modulo

# operator precidence

# as we have Bodmas rule in maths same as there is rule for maths in python where multiplication and division are priorities as compare toh subtraction and additon

#Comparison operator (return ans in true or false)
print(3<2);         #less then
print(3>2);         #greater then
print(3>=2);        #greater and equal
print(3<=2);        #less and equal
print(3==2);        #equals to
print(3==3);
print(3!=3);        #not euqals to
print(3!=2);

#Logical operator

print(2>3 or 2>1);          #if one is true then all are true
print(2>3 and 2>1);         #if one is false then all are false
print( not 2>1);            #convert false into true and viceversa

