# Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5

import random

random.randint(0, 100)

lst =[]

for i in range(100):
    lst.append(random.randint(0,100))



cisla = [1,2,3,5,3,10,54,20,45,2,2,4]
for cislo in cisla:
    if cislo % 5 == 0:
        print (cislo)
