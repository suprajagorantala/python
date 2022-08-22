#1.write a python program to print the pattern
        #* 
       #* * 
      #* * * 
     #* * * * 
    #* * * * * 
   #* * * * * * 
    #* * * * * 
     #* * * * 
      #* * * 
       #* * 
        #*
'''a = int(input("enter the value: "))
for i in range(1,a+1):
    if i == a:
        print("* "*a)
    else:
        spaces = " "*(a-i)
        stars = "* "*i
        print(spaces+stars)
for i in range(2,a+1):
    if i == 2:
        print(" "+"* "*(a-1))
    else:
        spaces = " "*(i-1)
        stars = "* "*(a-i+1)
        print(spaces+stars)'''
        
 #2.How would you check if each word in a string begins with a capital letter?
'''a = "Supraja Girl"
b = a.split()
for i in b:
    if i[0].isupper():
        print("yes")
    else:
        print("no")
#output:yes
yes'''
#3.Write a Python program that prints all the numbers from 0 to 6 except 4 and 5.
'''a = int(input("enter the number: "))
for i in range(0,6):
    if(i != 4)and(i != 5):
        print(i)
#output:enter the number: 6
0
1
2
3 '''
#4.Print list of elements and store in a another list and print  reverse order of list
'''a = [1,2,3,4,5]
b = []
for i in a:
    b.append(i)
print(b)
rev = b[::-1]
print(rev)
#output:[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]'''
#5.write a python program to print the pattern
            #A  
           #B C  
          #D E F  
         #G H I J  
        #K L M N O  
       #P Q R S T U
'''a = int(input("enter the number: "))
count = 65
k = 2*(a)-2
for i in range(0,a):
    for j in range(0,k):
        print(end = " ")
    k = k-1
    for j in range(0,i+1):
        alpha = chr(count)
        print(alpha,end =" ")
        count += 1
    print(" ")
    
enter the number: 6
          A  
         B C  
        D E F  
       G H I J  
      K L M N O  
     P Q R S T U  '''   
        
