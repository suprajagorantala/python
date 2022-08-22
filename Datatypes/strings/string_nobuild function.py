#1. WAP to print middle charactor of the string
'''
a = "supraja"
print("the middle character of stirng: ",a[3:4])
#output:the middle character of stirng:  r
'''
#2. WAP to print half reverse of the string 
#Input: KNOWLEDGE
#Output: EGDELKNOW
'''
a = "KNOWLEDGE"
first = a[5:]
second = a[:5]
print(first+second)
#output:EDGEKNOWL'''
#3.WAP to remove all the vouels from the given string
'''a = "supraja"
for i in a:
    if i == 'A'or i=='E'or i=='I'or i=='O'or i=='U'or i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
        a.replace(i,"")
    else:
        print(i,end=" ")
#output:s p r j '''
#4. WAP to insert * in front of every vouels in the string.
#Input: BANANA
#Output: B*AN*AN*A
'''a = "BANANA"
for i in a:
    if i == 'A'or i=='E'or i=='I'or i=='O'or i=='U'or i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
        print("*"+i,end="")
    else:
        print(i,end="")
#output:B*AN*AN*A'''
#5. WAP to count number of words in the string.
'''a = "sdfgerthu"
print("count no of words: ",len(a))
#output:count no of words:  9'''
#6. WAP to remove extra space from the given string
'''a = "s u p raja"
print(a.replace(" ",""))
#output:supraja'''
#7. WAP to insert string in between the given string
#Input: Ojas technologies 
#Output: Ojas innovative technologies
'''a = "ojas technologies"
b = "innovative"
print(a[:4]+" "+b+" "+a[5:])
#output:ojas innovative technologies'''
#8. WAP to find the ascci value of given char
'''a = input("enter a char: ")
print("the ASCII value of "+a+" is ",ord(a))
#outpur:enter a char: a
the ASCII value of a is  97'''
#9.insert ojas in front of every string
'''a = " supraja "
b = " gorantala "
c = "ojas "
print(c+a+c+b)
#output:ojas  supraja ojas  gorantala'''
#10. insert ojas in every extra space in the string
'''a = "s upraja gorantala"
b = "ojas"
print(a.replace(" ",b))
#output:sojasuprajaojasgorantala'''
        
