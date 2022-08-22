#1. How would you confirm that 2 strings have the same identity?
'''a = "supraja"
b = "asdfrgn"
print(id(a))
print(id(b))
print(a == b)
#output:2059777834672
2059777834736
False'''
#2. How would you check if each word in a string begins with a capital letter?
'''a = "Abghy Bhju cmkl"
b = a.split()
print(b)
for i in b:
    if i[0].isupper():
        print(i)
#output:Abghy
#Bhju'''
#3. Check if a string contains a specific substrin
'''string = "specific person"
substring = "eats"
if substring in string:
    print("found")
else:
    print("not found")
#output:not found '''
#4. Find the index of the first occurrence of a substring in a string
'''string = "this is a room of room"
print(string.index("room")) #index is used to find the first occurance of string and rindex() is used to find the last occurance of string
#output:10'''
#5. Count the total number of characters in a string
'''string = "efhutgn"
print(len(string))
#output:7'''
#6. Count the number of a specific character in a string
'''a = "she has long hair"
print(a.count('h'))
#output:3'''
#7. Capitalize the first character of a string
'''a = "supraja"
print(a[0].upper()+a[1:])
#output:Supraja'''
#8.What is an f-string and how do you use it?
'''f-string make string interpolation really easy
f-string is similar to using format()'''
#9. Search a specific part of a string for a substring
'''a = "the room is dark"
print(a.index('s'))
#output:10'''
#10. Interpolate a variable into a string using format()
a = "girl"
b = "supraja"
'this is a {} and name is {}'.format(a,b)
#11. Check if a string contains only numbers
'''a = '123'
if a.isnumeric():
    print("true")
else:
    print("false")
#output:true'''
#12. Split a string on a specific character
'''a = "this is a room"
print(a.split())
#output:['this', 'is', 'a', 'room']'''
#13. Check if a string is composed of all lower case characters
'''a = "asghu"
if a.islower():
    print("true")
else:
    print("false")
#output:true'''
#14. Check if the first character in a string is lowercase
'''a = "aSDgh"
if a[0].islower():
    print("yes")
else:
    print("no")
#output:yes'''
#15. Can an integer be added to a string in Python?
'''no,because it will occur "type error"'''
#16. Reverse the string “hello world”
'''a = "hello world"
print(a[::-1])
#output:dlrow olleh'''
#17. Join a list of strings into a single string, delimited by hyphens
'''a = "supraja"
print("-".join(a))
#output:s-u-p-r-a-j-a'''
#18. Check if all characters in a string conform to ASCI
'''a = "string"
print(a.isascii())
#output:true'''
#19. Uppercase or lowercase an entire string
'''a = "supraja"
if a.isupper():
    print("true")
else:
    print("false")
#output:false
'''
#20. Uppercase first and last character of a string
'''a = "supraja"
print(a[0].upper()+a[1:6]+a[6].upper())'''
#output:SuprajA
#21. Check if a string is all uppercase
'''a = "Supraja"
if a.isupper():
    print("true")
else:
    print("false")
#output:false'''
#22. When would you use splitlines()?
'''splitlines() method is used to split the lines at line boundaries. The function returns a list of lines in the string

Representation        Description

\n	            Line Feed
\r	            Carriage Return
\r\n	            Carriage Return + Line Feed
\x1c	            File Separator
\x1d	            Group Separator
\x1e	            Record Separator
\x85	           Next Line (C1 Control Code)
\v or \x0b	   Line Tabulation
\f or \x0c	   Form Feed
\u2028	           Line Separator
\u2029	          Paragraph Separator'''
#23. Give an example of string slicing
'''string = "adfrght"
print(string[:4])
#output:adfr'''
#24. Convert an integer to a string
'''
a = 789
b = str(a)
print(b)
print(type(b))
#output:789
<class 'str'>'''
#25. Check if a string contains only characters of the alphabet
'''a = "durgaprasad"
if a.isalpha():
    print("yes")
else:
    print("no")
#output:yes'''
#26. Replace all instances of a substring in a string
'''a = "this is a book and book contains pages"
print(a.replace('book','notes'))
#output:this is a notes and notes contains pages'''
#27. Return the minimum character in a string
'''a = "brg"
print(min(a))
output:b'''
#28. Check if all characters in a string are alphanumeric
'''a = "rdfe123"
if a.isalnum():
    print("true")
else:
    print("false")
#output:true'''
#29. Remove whitespace from the left, right or both sides of a string
'''a = "  this is a book  "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
#output:this is a book  
  this is a book
this is a book'''
#30. Check if a string begins with or ends with a specific character?
'''a = "city hyderabad"
print(a.startswith('c'))
print(a.endswith('a'))
#output:True
False'''
    




