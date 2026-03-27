class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructer = instructor
        self.students = []
        
    def enroll(self, name):
        self.students.append(name)
        print(f"{name} has been enrolled in {self.course} course.")
        
    def courseDetails(self):
        for student in self.students:
            print(f"Course: {self.course}, Instructor: {self.instructer}, Student: {student}")
    
    def completed(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed the {self.course} course.")
        else:
            print(f"{name} is not enrolled in the {self.course} course.")
            
    def averageGrade(self, grades):
        total = sum(grades)
        average = total / len(grades)
        print(f"The average grade for {self.course} course is: {average}")
        
course1 = input("Enter the course name: ")
name = input("Enter the instructor name: ")
student = input("Enter the student name: ")

course = OnlineCourse(course1, name)

# grades = [85, 90, 78, 92]

# course.averageGrade(grades)
# course.enroll(student)
# course.courseDetails()
# course.completed(student)

number_of_students = int(input("Enter the number of students: "))

for _ in range(number_of_students):
    student_name = input("Enter the student name: ")
    grades = []
    for _ in range(3):  # Assuming each student has 3 grades
        grade = float(input(f"Enter grade for {student_name}: "))
        grades.append(grade)
    student = OnlineCourse(course1, name)
    student.enroll(student_name)
    student.averageGrade(grades)
course.courseDetails()