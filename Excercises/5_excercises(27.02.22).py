#Write a program to get all vowels from given string
'''
a = "supraja"
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i == 'E' or i == 'I' or i=='O' or i=='U'):
        print(i)
#output:u
a
a
'''
#Write a program to calculate the simple interest
'''
p = int(input("enter the value: "))
t = int(input("enter the value: "))
r = int(input("enter the value: "))
print(p*t*r/100)

#output:enter the value: 2
enter the value: 3
enter the value: 4
0.24
'''
#Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N
'''
a = int(input("enter the value"))
numarater = 1
count = 0
total = 0
for i in range(1,a):
    count= count+1
    total = total+(numarater/count)
print(round(total))
#output: enter the value4
2
'''
#Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
'''
a = int(input("enter the value: "))
numarater = 1
fact = 1
total = 0
count = 0
for i in range(1,a):
    fact = fact*i
    count = count+1
    total = total+(numarater/fact)
print(round(total))
#output:enter the value: 3
2
'''
#Python Program to Replace All Occurrences of ‘a’ with $ in a String
'''
a = "supraja"
for i in a:
    if(i == 'a'):
        print("$")
    else:
        print(i)

#output:s
u
p
r
$
j
$
'''
    
   



