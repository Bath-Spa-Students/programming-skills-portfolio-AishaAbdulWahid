'''Write a python program that takes courses marks as input and then calculates average of all the 
   courses. After calculating the average, calculate the percentage of a student using total marks. Assume 
   the total of all the courses marks is 500 or take the total marks from the user as input.'''

# Get the number of courses
num_courses = int(input("Enter the number of courses: "))

# Get course marks
course_marks = []
for i in range (num_courses):
    marks = int(input("Enter the marks for the course {i+1}: "))   # this line asks the user to input the mark for each course.
    course_marks.append(marks)   # the append() function is used to add this mark to the course_marks list.

# Calculate the average
total_marks = sum(course_marks)
average = total_marks / len(course_marks)  # calculates the average marks by dividing the total marks by the lenght of course_marks.

# Calculate the percentage
percentage = (average/500) * 100

# Print the results
print(f"Total marks: {total_marks}")
print(f"Average marks: {average}")
print(f"Percentage: {percentage}%")

      
