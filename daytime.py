import time
time2 = time.strftime("%H:%M:%S")
print(time2)
time1= int(time.strftime("%H"))
# print(time)
if 4<time1<12:
    print("Good morning sir!")
elif 12<time1<18:
    print("Good afternoon sir!")
else :
    print("Good night sir!")