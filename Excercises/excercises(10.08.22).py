#1.Display square and perfect square root of numbers from 48 to 82. using list Comprehension.
'''b =[(i*i,i) for i in range(48,82) ]
print(b)

#output:[(2304, 48), (2401, 49), (2500, 50), (2601, 51), (2704, 52), (2809, 53), (2916, 54), (3025, 55), (3136, 56), (3249, 57), (3364, 58), (3481, 59), (3600, 60), (3721, 61), (3844, 62), (3969, 63), (4096, 64), (4225, 65), (4356, 66), (4489, 67), (4624, 68), (4761, 69), (4900, 70), (5041, 71), (5184, 72), (5329, 73), (5476, 74), (5625, 75), (5776, 76), (5929, 77), (6084, 78), (6241, 79), (6400, 80), (6561, 81)]
'''
#2.Display square and perfect square root of numbers from 48 to 82. using dictionary Comprehension.

'''b = {(i*i,i) for i in range(48,82)}
print(b)

#output:
{(4356, 66), (2916, 54), (2809, 53), (5041, 71), (3721, 61), (2704, 52), (4489, 67), (6241, 79), (3025, 55), (2304, 48), (2601, 51), (3364, 58), (6561, 81), (2500, 50), (5476, 74), (4624, 68), (4900, 70), (6084, 78), (3600, 60), (5625, 75), (3136, 56), (5776, 76), (5929, 77), (6400, 80), (5329, 73), (4096, 64), (3969, 63), (5184, 72), (3481, 59), (4225, 65), (3844, 62), (2401, 49), (3249, 57), (4761, 69)}'''

#.if the square of number inside list is divisible by 2 print the num.(1st question's answer should be taken as a list)
##for i in range(48,82):
##    b = i*i
##    if (b%2==0):
##        print(b,end=" ")
   
'''print([(i**2) for  i in range(48,82) if (i**2)%2 ==0])

#output:[2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400]''''

