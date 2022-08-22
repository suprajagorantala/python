#1.Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
#Input:
#[19, 19, 15, 5, 3, 5, 5, 2]
#Output:
#True
'''nums = [19,19,15,5,3,5,5,2]
print(nums)
if(nums.count(19)==2 and nums.count(5)>=3):
    print("true")
else:
    print("false")

#output:[19, 19, 15, 5, 3, 5, 5, 2]
true'''

#2.WAPP to check a given list of integers where the sum of the integers is equal to length of list.
'''list = [1,1,1]
total = 0
print(len(list))
for i in list:
    total+=i
if(total == len(list)):
    print("true")
else:
    print("false")

#output:
3
true'''

#3.WAPP to add two integers without using arithmetic operator
'''number = int(input("enter the number: "))
number2 = int(input("enter the number: "))
count = 0
count1 = 0
sum = 0
for i in range(number):
    count+=1
for i in range(number2):
    count1+=1
sum += sum+count+count1
print(sum)

#output:enter the number: 5
enter the number: 6
11'''




    
        

    
    
