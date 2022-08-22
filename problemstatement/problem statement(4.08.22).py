 #Write a Python program to find the strings in a given list, starting with a given prefix.
#Input:
#[( ca,('cat', 'car', 'fear', 'center'))]
#Output:
#['cat', 'car']
#Input:
#[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
#Output:
#['dog', 'donut']
'''a = ['cat','car','fear','center']
b=[]
for i in a:
    if(i[0]=='c')and(i[1]=='a'):
        b.append(i)
print(b)
#output:['cat', 'car']'''
