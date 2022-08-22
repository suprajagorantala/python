#1.  Add a list of elements to a given set
'''a = ["apple","banana","cherry"]
b = set()
for i in a:
    b.add(i)
print(b)

#output:{'banana', 'cherry', 'apple'}'''

#2. Return a set of identical items from a given two Python
'''a = {"sai","shiva","renu","renuka"}  #identical--->common elements of two sets
b = {"ramu","sai","shiva","priya"}
print(a&b)

#output:{'sai', 'shiva'}'''

'''a = {"sai","shiva","renu","renuka"}
b = {"ramu","sai","shiva","priya"}
c = set()
for i in a:
    if i in b:
        c.add(i)
print(c)

#output:{'sai', 'shiva'}'''

#3.Returns a new set with all items from both sets by removing duplicates
'''a = {1,2,3,4}
b = {2,5,7,8}
print(a|b)

#output:{1, 2, 3, 4, 5, 7, 8}'''

'''a = {1,2,3,4}
b = {2,5,7,8}
c = set()
for i in a:
    if i in b:
        c.add(i)
    else:
        c.add(i)
for i in b:
    if i in a:
        c.add(i)
    else:
        c.add(i)
print(c)

#output:{1, 2, 3, 4, 5, 7, 8}'''

#4.Given two Python sets, update first set with items that exist only in the first set and not in the second set.
'''a = {1,2,3,4}
b = {2,7,8}
print(a-b)

#output:{1, 3, 4}

a = {1,2,3,4}
b = {2,7,8}
c = set()
for i in a:
    if i not in b:
        c.add(i)
print(c)

#output:{1, 3, 4}'''

#5.Remove 10, 20, 30 elements from a following set at once
'''a ={10,20,30,40,50}
b = {10,20,30,40}
a.difference_update(b) #difference_update will remove the morethan one common elements
print(a)

#output:{50}'''

'''a = {10,20,30,40,50}
b = {10,20,30,40}{1, 4, 5, 6, 8, 9}
c = set()
for i in a:
    if i in b:
        break
    else:
        c.add(i)
print(c)

#output:{50}'''

#6.Return a set of all elements in either A or B, but not both
'''a ={1,2,3,4,6}
b ={2,3,5,8,9}
print(a^b)

#output:{1, 4, 5, 6, 8, 9}'''

'''a = {1,2,3,4,6}
b = {2,3,5,8,9}
c =set()
for i in a:
    if i not in b:
        c.add(i)
for i in b:
    if i not in a:
        c.add(i)
print(c)

#output{1, 4, 5, 6, 8, 9}'''

#7.Determines whether or not the following two sets have any elements in common. If yes display the common elements
'''a={1,2,3,4}
b={3,6,7,8}
if(a.isdisjoint(b)): #isdisjoint---> when we comparing two lists if any comman element is there then it prints "false" otherwise "true"
    print("no")
else:
    print("Yes")
    print(a&b)
#output:Yes
{3}'''

#8.Update set1 by adding items from set2, except common items
'''a = {1,2,3,4}
b ={3,4,5,6}
a.symmetric_difference_update(b)
print(a)

#output:{1, 2, 5, 6}'''

#9.Remove items from set1 that are not common to both set1 and set2
'''a ={1,2,3,4}
b = {3,4,5,6}
a.intersection_update(b)
print(a)'''

#10.Write a Python program to check if a given set is superset of itself and superset of another given set
'''a = {1,2,34,5}
b = {4,5,7,8}
print(a.issuperset(a))
print(a.issuperset(b))

#output:True
False'''
#11.Write a Python program to check a given set has no elements in common with other given set
'''a = {1,2,3,4}
b = {4,6,7,8}
for i in a:
    if i in b:
        print("false")
    
#output:false'''

#12.Write a Python program to remove the intersection of a 2nd set from the 1st set.

'''a = {1,2,3,4}
b = {3,4,5,6}
b.difference_update(a)
print(b)

output:{5, 6}'''

#13. Perform all sets methods by taking an example of your own.

#add():adding the elements in a set
'''a = {1,2,3,4}
c = set()
for i in a:
    c.add(i)
print(c)

#output:{1, 2, 3, 4}'''
#clear():Removes all the elements from the set
'''a = {1,2,3,4}
a.clear()
print(a)

#output:set()'''
#copy():Returns a copy of the set
'''a = {1,2,3,4}
b = a.copy()
print(b)

#output:{1, 2, 3, 4}'''
#difference():returns a set that containing differnce between two sets
'''a ={1,2,3,5}
b ={2,7,8,9}
c = a.difference(b)
print(c)

#output:{1, 3, 5}'''

#difference_update():removes common element of set
'''a = {1,2,3,4}
b = {2,4,5,6}
a.difference_update(b)
print(a)

#output:{1, 3}'''
#discard():Remove the specified item
'''a ={1,2,3,4}
a.discard(2)
print(a)

#output:{1, 3, 4}'''

#intersection():Returns a set, that is the intersection of two or more sets
'''a = {1,2,3,4}
b = {2,3,6,7}
c = a.intersection(b)
print(c)
#output:{2, 3}'''

#intersection_update():Removes the items in this set that are not present in other, specified set(s)
'''a = {1,2,3,4}
b ={3,4,5,6}
a.intersection_update(b)
print(a)
#output:{3, 4}'''

#isdisjoint():Returns whether two sets have a common element or not ,if common element is there then it return false otherwise it returns true.
'''a = {1,2,3,4}
b = {4,5,6,7}
print(a.isdisjoint(b))

#output:False'''
#issubset():Returns whether another set contains this set or not

'''a = {1,2,3,4}
b = {4,3,7,8}
print(a.issubset(b))

#output:false'''

#issuperset():Returns whether this set contains another set or not
'''a = {1,2,34,5}
b = {1,2,34,5}
print(a.issuperset(b))   

#output:True'''
#pop():Removes an element from the set randomly.
'''a = {1,2,3,4}
a.pop()
print(a)

#output:{2, 3, 4}'''

#remove():Removes the specified element.
'''a = {1,2,3,4}
a.remove(2)
print(a)

#output:{1, 3, 4}'''

#symmetric_difference():Returns a set with the symmetric differences of two sets
'''a = {1,2,3}
b = {3,4,5}
print(a^b)

#output:{1, 2, 4, 5}'''

#symmetric_difference_update():inserts the symmetric differences from this set and another
'''a = {1,2,3}
b = {3,4,5,6}
a.symmetric_difference_update(b)
print(a)

#output:{1, 2, 4, 5, 6}'''
#union():Return a set containing the union of sets
'''a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)

#output:{1, 2, 3, 4, 5, 6}'''
#update():Update the set with another set, or any other iterable
'''a = {1,2,3,4}
b = {45,67,89}
a.update(b)
print(a)

#output:{1, 2, 3, 4, 67, 89, 45}'''


