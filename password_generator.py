import random
Uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase="abcdefghijklmnopqrstuvwxyz"
password=""
length=int(input("enter the length of password"))
for i in range(length):
    password+= random.choice(Uppercase) + random.choice(Lowercase)
password = password[:length]
print("password generated ")
print(password)

