#List

subjects = ["C","C++","C#","Java","C"]
''' P-1
print(subjects)
print(subjects[0])
print(subjects[-2])
print(subjects[1:])'''
'''
#P-2
print("Python" in subjects)
print("Java" in subjects)
print("java" in subjects)
print("Swift" not in subjects)'''
'''
print(subjects + ["Swift",34])#Connecting last
subjects.append("Swift")#same
print(subjects)

subjects.insert(3,"TOC")#connecting middle
print(subjects)
subjects.remove("C")#Removes specific item
print(subjects)
subjects.sort()
print(subjects)

subjects.pop()
subjects.pop()#Removes last item
print(subjects)
subjects.clear()
print(subjects)
#print(subjects * 2)'''

subjects2 = subjects.copy()
print(subjects2)

pos = subjects.index("C")
print(pos)
pos2 = subjects.count("C")
print(pos2)

