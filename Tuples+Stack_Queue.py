'''
#Tuples
students = (

     ("Anisul Islam",67,56.5),
     "Atanu Barua",
     "Rajib"
)

print(students[1:])'''
#Sets
'''
#num1 = {1,2,3,4,5,8}
#num2 = set([4,5,6])
#num2.add(7)

#num2.remove(4)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)'''
#Stack+Queue
'''
books = [ ]
books.append("Learn C")#push func
books.append("Learn C++")
books.append("Learn Swift")

books.pop()#pop func-LIFO(Last in First out)
books.pop()

print("Now the top book is : ",books[-1])
books.pop()
if not books:
	print("No books left")'''
from collections import deque
bank = deque(["Atanu","Roktim","Tanim"])
bank.popleft()
bank.pop()
bank.pop()
print(bank)

if not bank:
	print("No person")	
	
print("Fin")
