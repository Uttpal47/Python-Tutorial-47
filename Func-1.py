#function
'''def add(a,x):
	sum = a + x
	print(sum)
	
def sub(a,x):
	res = a - x
	print(res)'''
	
def mul(a,x):
	res = a * x
	return res
		
result2 = mul(4,50.8)
print("Result is = ",result2)

#
def large(a,x):
	if a>x:
		return a
	else:
		return x

Max = large
print("Result = ",Max(50,60))

print("Fin")