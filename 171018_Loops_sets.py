#!/usr/bin/env python3

count = 0
while count < 101:
  print("count:", count)
  count+=1
#Defining count with while loop

numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
    if num %2 == 0:
        print (num)
#Sorting even values in a list with modulus

numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
    if num %2 == 0:
        even_sum += num
print (even_sum)

numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
    if num %2 != 0:
        odd_sum += num
print (odd_sum)
#Summary of even and odd values (may not work)

numbers = [101,2,15,22,95,33,2,27,72,15,52]
print (numbers)
print (numbers.pop()) #removing arbitrary number from list
print (numbers) #comparing new list to original

numbers = [101,2,15,22,95,33,2,27,72,15,52]
print (numbers)
print (numbers.remove(95)) #removing 95 from list
print (numbers) #comparing new list to original
#pop and remove from the list

for num in range (0,100):
    print (num)
#Using range in for loop to print numbers

for numin range (0,100):
    print (num)
    count +=1
    if count == 100:
        continue
    print ('loop added correctly')
#Still working on this problem...

