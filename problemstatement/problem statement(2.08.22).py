#2<=n<=10
#0<=marks[i]<=100
#length of marks arrys=3
#The query_name is 'beta'. beta's average score is .
#Input Format
#The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
#Constraints
#Output Format
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#Sample Input 0
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
#Sample Output 0
#56.00
#Explanation 0
#marks for Mallika are{52,56,60} whose average is ((52+56+60)/3)=56
#Marks for Malika are  whose average is 
#Sample Input 1
#2
#Harsh 25 26.5 28
#Anurag 26 28 30
#Harsh
#Sample Output 1
#26.50
#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
''' 
krishna = [67,68,69]
Arjun = [70,98,63]
malika = [52,56,60]
krishna_sum = 67+68+69
krishna_avg = krishna_sum/3
print(round(krishna_avg))
Arjun_sum = 70+98+63
Arjun_avg = Arjun_sum/3
print(round(Arjun_avg/3))
malika_sum = 52+56+60
malika_avg = malika_sum/3
print(round(malika_avg))
if(krishna_avg<Arjun_avg)and(krishna_avg<malika_avg):
    print("the minimal avg of krisha: ",krishna_avg)
elif(Arjun_avg<krishna_avg)and(Arjun_avg<malika_avg):
    print("the minimal avg of Arjun: ",Arjun_avg)
else:
    print("the minimal avg of malika: ",malika_avg)
#output:68
26
56
the minimal avg of malika:  56.0                       
'''
