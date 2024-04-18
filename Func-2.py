#xargs(x-arguments)

'''def student(*details):
	print(details[-1])

student(101,"Atanu",3.75)
student(1056,"Atashi",3.85)
#x-args works like tuples

def add(*numbers):
	sum = 0
	for num in numbers:
		sum = sum + num


	print("Res is = ",sum)

add(10,30)
add(39,50,60)
add(50,55,45,67,44)'''

# xx-args
def student(**details):
	print(details)

#xx-args work like dictionary(key-value pairing)

student(id=107,name = "Atanu",cGPA=4.0)



