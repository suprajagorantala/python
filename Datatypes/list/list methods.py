#list methods

#append():Adds an element at the end of the list
'''a = ["sai","veena"]
b = a.append("sup")
print(a)

#output:['sai', 'veena', 'sup']'''


#clear():Removes all the elements from the list
'''a = [1,2,3,4]
b = a.clear()
print(a)

#output:[]'''

#copy():Returns a copy of the list
'''a = [1,2,3]
b = a.copy()
print(b)

#output:[1, 2, 3]'''

#count():Returns the number of elements with the specified value

'''a =[1,2,3,2,2]
print(a.count(2))

#output:3'''

#extend():Add the elements of a list (or any iterable), to the end of the current list

'''a =[1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#output:[1, 2, 3, 4, 5, 6]'''

#index():return the position of the element in a given list

'''a = ["asd","sdf","lkj","ghj"]
print(a.index("lkj"))

#output:2'''

#insert():adding the element at specified position

'''a = ["asd","sdf","lkj","ghj"]
a.insert(2,"rty")
print(a)

#output:['asd', 'sdf', 'rty', 'lkj', 'ghj']'''

#pop():Removes the element at the specified position,if pop()-->removes last element of string,if pop(2)-->removes the specific postion of elements removed in list

'''a =["asd","ert","fgh"]
a.pop()
print(a)

#output:['asd', 'ert']'''

'''a =["asd","ert","fgh"]
a.pop(1)
print(a)

#output:['asd', 'fgh']'''

#remove():Removes specific element in the list

'''a =["asd","ert","fgh"]
a.remove("ert")
print(a)

#output:['asd', 'fgh']'''

#reverse():Reverses the order of the list

'''a = [3,4,7,9,8]
a.reverse()
print(a)

#output:[8, 9, 7, 4, 3]'''

#sort():Sorts the list from ascending to decending

'''a = [5,79,3,1,4]
a.sort()
print(a)

#output:[1, 3, 4, 5, 79]'''

