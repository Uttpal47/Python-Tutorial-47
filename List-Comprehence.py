#list comprehensions(P-1)

num = [1,2,3,4,5,6,7]
'''
res = list(map(lambda x: x*x,num))
print(res)'''

#[expression for item in list]

task = [x*x for x in num]

print("Answer is = ",task)
#Part -2
'''
task = list(filter(lambda x: x%2!=0,num))
print("Answer is = ",task)'''

task2 = [x for x in num if x%2!=0]
print("Ans is = ",task2)