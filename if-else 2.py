
#If application
'''
num1 = float(input("Enter the number = "))
num2 = float(input("Enter the number = "))
num3 = float(input("Enter the number = "))


if num1 > num2:
	print("largest is ",num1)
else:
	print("largest is ",num2)
'''
#ternary(three) operator

#print(num1 if num1>num2 else num2)
#Logical operator

'''
if num1 > num2 and num1 > num3:
	print("Largest num is ",num1)
if num2 > num1 and num2 > num3:
	print("Largest num is ",num2)

else:
	print("Large is ",num3)'''
#Vowel/conso

ch = str(input("Enter char : "))

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
	print("Vowel")

else:
	print("Consonant")
	
print("Finito")