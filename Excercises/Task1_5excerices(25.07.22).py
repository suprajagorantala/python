#WAP for eligibility of a canditate voter_id, suppose age between (18 to 80 years old) using flow control conditions?
'''
number = int(input("enter the age: "))
if(number>18)and(number<=80):
    print("The candiate is eligible for voter_id ",number)
else:
    print("the candiate is not eligible for voter_id ",number)
    
#output: enter the age: 25
The candiate is eligible for voter_id  25
enter the age: 5
the candiate is not eligible for voter_id  5
'''
#---------------------------------------------------------------------------
#WAP for calculating student marks in 5-subjects,and find  grades,(suppose grade A,B,C and Fail)?
'''
name = input("enter the name: ")
first_subject = int(input("enter the first_subject marks: "))
second_subject = int(input("enter the second_subject marks " ))
third_subject = int(input("enter the thrid_subject marks "))
fourth_subject = int(input("enter the fourth_subject marks "))
fivth_subject = int(input("enter the fivth_subject marks "))

total = first_subject+second_subject+third_subject+fourth_subject+fivth_subject
avg = total/5
print(avg)
if(avg>60)and(avg<=80):
    print("Grade A")
elif(avg>40)and(avg<=60):
    print("Grade B")
elif(avg>=30)and(avg<=40):
    print("Grade c")
else:
    print("Fail")
#output:enter the name: supraja
enter the first_subject marks: 12
enter the second_subject marks 13
enter the thrid_subject marks 15
enter the fourth_subject marks 14
enter the fivth_subject marks 16
14.0
Fail
 '''
#----------------------------------------------------------------------
#WAP for finding  even or odd number using (if .. else ... condition)?
'''
number = int(input("enter the number: "))
if(number<0):
    print("not a valid number")
elif(number%2 == 0):
        print("print the even number")
else:
    print("print the odd number")

#ouput:enter the number: 24
print the even number

enter the number: -12
not a valid number
'''
#----------------------------------------------------------------------------
#WAP calculating area of a circle, result in positive integers only not in float values (hint: pi=3.14,using int() function)?
'''
radius = int(input("enter the number: "))
Area_of_circle = 3.14 * (radius * radius)
print(round(Area_of_circle))

#output:enter the number: 2
13
'''
#-------------------------------------------------------------------------------
#WAP for finding  variables A and B are having the same memory location?
'''
a = int(input("enter the value: "))
b = int(input("enter the value: "))
if id(a) == id(b):
    print("the memory location is same")
else:
    print("the memory location is different")

#output:enter the value: 10
enter the value: 10
the memory location is same

enter the value: 10
enter the value: 12
the memory location is different
'''
#------------------------------------------------------------------------
