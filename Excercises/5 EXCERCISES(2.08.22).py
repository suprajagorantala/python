#1.Calculate income tax for the given income by adhering to the below rules
#Taxable Income    Rate (in %)
#First $10,000    0
#Next $10,000    10
#The remaining    20
#Expected Output:
#For example, suppose the taxable income is 45000 the income tax payable is
#10000*0% + 10000*10%  + 25000*20% = $6000.
'''a = int(input("enter the salary: "))
if(a>0)and(a<10000):
    print("no income tax")
elif(a>10000)and(a<20000):
    a = a-10000
    r = a*0.01
    print("tax will be: ",r)
elif(a>20000):
   tax_payable = 0
   tax_payable = 10000 * 10 / 100
   tax_payable += (a - 20000) * 20 / 100
print("Total tax to pay is", tax_payable)
   
#output:enter the salary: 45000
Total tax to pay is 6000.0'''
#2.Count the length of list with out using any inbuilt function.

'''a = [1,2,3,4,5]
count = 0
for i in a:
    count += 1
print("length: ",count)
#output:length:  5 '''
#3.Write a Python program to create a histogram from a given list of integers.
'''a =[1,3,5,7,8]
for i in a:
    print("x"*i)
#output:x
xxx
xxxxx
xxxxxxx
xxxxxxxx'''
#4. Take input from user and if input is string print String
#if input is integer/float print integer
#if input is mix of string and integer print Error
#HINT Can be done using ASCII code
'''inpt=input("Enter the string ")
int_counter=0
str_counter=0
for i in inpt:
    if ord(i)>48 and ord(i)<57:
        int_counter+=1
    elif (ord(i)>97 and ord(i)<122) or (ord(i)>65 and ord(i)<90) :
        str_counter+=1

if int_counter >0 and str_counter ==0:
    print("Integer")
elif int_counter == 0 and str_counter >0:
    print("String")
else:
    print("Error")
#output:
    Enter the string supraja
String
'''
#5.Python program to check if a string is palindrome or not
'''ip=input("enter word:")
r=ip[-1::-1]
if r==ip:
    print("palindrome")
else:
    print("not palindrome")
#output:enter word:sus
palindrome'''
