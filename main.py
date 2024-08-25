import random

code = random.randint(1000,100000000001)

tries = 0

inputed_code = 1000

while(inputed_code!= code):
    inputed_code+=1
    tries+=1
print(f"The password is {inputed_code} and took {tries} tries")    