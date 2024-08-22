# Write a program to accept mark of 6 students and display them in a sorted manner

# Declare empty list of marks
marks = []

# Store marks of 6 students
m1 = int(input("Enter marks : "))
marks.append(m1)
m2 = int(input("Enter marks : "))
marks.append(m2)
m3 = int(input("Enter marks : "))
marks.append(m3)
m4 = int(input("Enter marks : "))
marks.append(m4)
m5 = int(input("Enter marks : "))
marks.append(m5)
m6 = int(input("Enter marks : "))
marks.append(m1)

# Print sorted list
marks.sort()
print(f"Marks : {marks}")

'''
Enter marks : 83
Enter marks : 47
Enter marks : 83 
Enter marks : 83
Enter marks : 38
Enter marks : 38
Marks : [38, 47, 83, 83, 83, 83]
'''
