# list is collection of items

marks = [50,45,60,85,95,100,90]

marks.clear()
print(marks)
print(marks)
print(marks[3])
#negatice index also there in python
print(marks[-1])
print (marks[0:2])
print(marks[1:4])

# printing with the help of for loop
for score in marks:
    print(score)


marks.append(99)
# marks.insert(1,98)
print(marks)
print(99 in marks)
print(len(marks))


# printing with the help of while loop 
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1 


marks_Ramu = str([50,45,60,85,95,100,90])
print("Marks of Ramesh are:" + " " + marks_Ramu)



