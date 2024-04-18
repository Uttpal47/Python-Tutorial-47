'''
num = list(range(20))
print(num)
print(num[19])

num2 = list(range(5,15))
print(num2)

num3 = list(range(0,51,2))
print(num3)'''

#Iteration + sum using loop
'''
num = [10,20,30,40]
sum = 0

print(num)

index = 0
n = len(num)
while index<n :
	print(num[index])
	index = index + 1

for x in num:
	sum = sum + x
print("Summation is :",sum)'''
#series
n = int(input("Enter the last num : "))
sum = 0
#1*1+2*2+.....+n*n
for x in range(1,n+1,1):
	sum = sum + 1/x
		
print("Summation is :",sum)

#prime-number+GCD+LSD








