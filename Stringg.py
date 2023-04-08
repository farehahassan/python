# name = input("Enter your name : " )
# print("Welcome " + name )     #concatinating two strings (place together)

# me = "fareha"
#here f is at index 0 , a is at 1 , r is at 2 , and so on
# print(me[0])        #these square brackets represent that it's an array

# print(me[0:3])      #3 does not included
# print(me[0:-1])        #if we don't know the length of array then we just write -1 but same as before last letter not included
# print(me[:6])          #same as [0:6]
# print(me[0:])          #same as [0:6]
# print(me[0: : 2])       #this will print name but remove one letter alternativly

#String functions

blog = "hey I am fareha hassan a software engineering and currently learning python programming"

print(len(blog))        #length of varibale
print(blog.endswith("ing"))         #wethear the string ends with given word or not
print(blog.count("g"))              #counts the letter we given is present or not
print(blog.capitalize())