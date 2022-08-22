#Q1.WAP in python arrange string characters such that lowercase letters should come first
'''
a = "SUPrAJA"
lower =[]
upper =[]
for i in a:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
add = " ".join(lower+upper)
print(add)

#output:r S U P A J A
'''
#WAP to print sum of prime numbers in given list input :- 2 4 5 6 7 3 8 output :- 17
'''
a = [ 2, 4, 5, 6, 7, 3, 8]
sums = 0
for i in a:
    prime = 0
    for j in range(2,i-1):
        if i % j == 0:
            prime += 1
    if prime == 0 and i != 1:
        sums +=i
print(sums)
#output:17'''

#WAP in python remove all characters from a string except integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )
'''
a = "H56U1E9JIG314w2"
b=""
for i in a:
    if i.isdigit():
        b+=i
print(b)
#56193142
'''
#WAP to take a list and find the possition of the item .(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)
'''
list = [45,12,66,2,33]
length = len(list)
for i in list:
    print(list.index(i))
#output:0
1
2
3
4   
'''
or
'''
list =[45,12,66,2,33]
print(list.index(66))
output:2
'''
#when do we use nested for loop.Write an example.
'''
The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''        

        
            
    
