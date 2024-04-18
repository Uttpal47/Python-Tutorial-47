#Normal func
def calc(a,b):
	sum = a*a + 2*a*b +b*b
	return sum

print("Result = ",calc(1,2))

#Lamda func

sum = ((lambda  a,b : a*a + 2*a*b +b*b )(2,3))
#a,b-parameters; expression:a*a + 2*a*b +b*b

print("Result is = ",sum)

#Map function-need two parameters(func,iterl)

#iterl-list ke bujhai
def sq(x):
	mul = x*x
	return mul

num = [1,2,3,4,5]

result = list(map(sq,num))

print("Ans is = ",result)

#Filter func-also works with iterl objs;
#Er kaj hocce filtering kora

num = [1,2,3,5,6,8,24]

task = list(filter(lambda x: x%2!=0,num))

print("Answer is = ",task)

#Zip Func: onekgolo func ke combine kore single list e transform kora

roll = [101,102,103,105]

name = ["Atanu", "Atashi", "Bimal", "Urmi"]

tasks = list(zip(roll,name,"ABCCBA"))

print("Answers are : ",tasks)
