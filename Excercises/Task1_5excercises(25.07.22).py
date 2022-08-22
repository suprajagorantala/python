#1.WAP to reverse a number
'''
number = int(input("enter the number: "))
rev = 0
while(number>0):
    rem = number%10
    rev = (rev*10)+rem
    number = number//10
print(rev)

#output:enter the number: 123
321
'''
# WAP to count  the number  occurrence/frequency  of a  each character in a string
'''
string = input("please enter string: ")
char = input("enter the string: ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count+1
print(count)

#output:please enter string: supraja
enter the string: a
2
'''

#WAP  to check length of two string is equal or not
'''
a = input("enter the string: ")
b = input("enter the string: ")
if(len(a) == len(b)):
    print("legths are equal")
else:
    print("lengths are not equal")
#output:enter the string: supraja
enter the string: ramadev
legths are equal
'''
#Python program to print even numbers up to 100
'''
number = int(input("enter the number: "))
for i in range(1,number+1):
    if(i%2 == 0):
        print(i)
    else:
        i = i+1

#output:enter the number: 100
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
'''
#Write a program in python to find greatest among three integers
'''
a= int(input("enter a number"))
b= int(input("enter a number"))
c= int(input("enter a number"))
if(a>b)and(a>c):
    print("the gretest number",a)
elif(b>a)and(b>c):
    print("the gretest number",b)
else:
    print("the gretest number",c)

#output:enter a number1
enter a number5
enter a number8
the gretest number 8
'''
