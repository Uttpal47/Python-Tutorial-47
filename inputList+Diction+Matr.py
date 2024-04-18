#list input
'''try:
	n = input("Enter a text of numbers : ")
	
	list = n.split()
	sum = 0
	
	for num in list:
		sum = sum + int(num)
		
	print("Ans is :",sum)'''

#Turning strings into nums:
	
try:
	numOfWords = 0
	numOfLetters = 0
	numOfDigits = 0
	
	text = input("Enter a text of numbers : ")
	
	for x in text:
		x = x.lower()
		if x >= 'a' and x <= 'z':
			numOfLetters = numOfLetters + 1
			
		elif x >= '0' and x <= '9':
			numOfDigits = numOfDigits + 1
			
		elif x == ' ':
			numOfWords = numOfWords + 1
			
	print("Num of letters :",numOfLetters)
	print("Num of digits :",numOfDigits)
	print("Num of words :",numOfWords+1)
	
	

except (ValueError,IndexError,NameError):
		print("You entered incorrect value")


'''matrix = [
        [1,2,3],
        [4,5,7],

]
matrix[0] [2] = 40
print(matrix[0] [2])'''
#mtrix row/coloum num starts frm 0,,

#Dictionaries
'''studentId = {
         101 : "Atanu",
         102 : "Wahid",
         103 : "Tanim",

}
#print(studentId[103])
#print(studentId)
#print(studentId.get(106,"Not Valid"))'''
