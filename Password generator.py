import random
import string
a=int(input("Enter the length of password:"))
ch=string.ascii_letters+string.digits+string.punctuation
password=' '
for i in range(a):
  x=random.choice(ch)
  password+=x
print(password)