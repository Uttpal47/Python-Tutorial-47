#Guess game
import random
try:
	for x in range(1,8):
	 guessNum = int(input("Enter your guess between 1 to 5 : "))
	 randomNum = random.randint(1,5)
	
	 if guessNum == randomNum:
		 print("You won")
	 else:
		 print("You lose")
		 print("Random number was = ",randomNum)
	
except (ValueError,IndexError):
		print("You entered incorrect value")
		
		
		
a = 20
b = 10
a, b = b, a
print("a =",a)
print("b =",b)
