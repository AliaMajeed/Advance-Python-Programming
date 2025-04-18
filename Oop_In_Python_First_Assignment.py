class User:
    def __init__(self, name, email, gender, user_id):
        self.name = name
        self.email = email
        self.gender = gender
        self.user_id = user_id

    def generate_report(self):
        raise NotImplementedError("Subclasses must implement generate_report")


class Student(User):
    def __init__(self, name, email, gender, user_id, roll_no, semester, enrolled_courses=None, grades=None):
        super().__init__(name, email, gender, user_id)
        self.roll_no = roll_no
        self.semester = semester
        self.enrolled_courses = enrolled_courses if enrolled_courses else []
        self.grades = grades if grades else {}

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.name} enrolled in {course.title}")

    def view_grades(self):
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")

    def generate_report(self):
        print(f"Student Report: {self.name} (Roll No: {self.roll_no})")
        print(f"Semester: {self.semester}")
        print(f"Enrolled Courses: {[course.title for course in self.enrolled_courses]}")
        print(f"Grades: {self.grades}")
        print("-" * 50)


class Teacher(User):
    def __init__(self, name, email, gender, user_id, employee_id, department, assigned_courses_list=None):
        super().__init__(name, email, gender, user_id)
        self.employee_id = employee_id
        self.department = department
        self.assigned_courses_list = assigned_courses_list if assigned_courses_list else []

    def assign_grade(self, student, course, grade):
        student.grades[course.course_code] = grade
        print(f"{self.name} assigned grade {grade} to {student.name} for {course.title}")

    def generate_report(self):
        print(f"Teacher Report: {self.name} (Employee ID: {self.employee_id})")
        print(f"Department: {self.department}")
        print(f"Assigned Courses: {[course.title for course in self.assigned_courses_list]}")
        print("-" * 50)


class Course:
    def __init__(self, course_code, title, credit_hours, teacher):
        self.course_code = course_code
        self.title = title
        self.credit_hours = credit_hours
        self.teacher = teacher
        self.student_list = []

    def enroll_student(self, student):
        if student not in self.student_list:
            self.student_list.append(student)
            student.enroll(self)

    def show_summary(self):
        print(f"Course Title: {self.title}")
        print(f"Course Code: {self.course_code}")
        print(f"Credit Hours: {self.credit_hours}")
        print(f"Teacher: {self.teacher.name}")
        print("Enrolled Students:")
        for student in self.student_list:
            print(f" - {student.name} (Roll No: {student.roll_no})")
        print("-" * 50)


class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.courses = []


class University:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def register_student(self, department, student):
        department.students.append(student)

    def hire_teacher(self, department, teacher):
        department.teachers.append(teacher)

    def add_course(self, department, course):
        department.courses.append(course)

    def enroll_student_in_course(self, student, course):
        course.enroll_student(student)


# SAMPLE DATA

# University
university = University()

# Departments
cs_dept = Department("CS")
it_dept = Department("IT")
se_dept = Department("SE")

university.add_department(cs_dept)
university.add_department(it_dept)
university.add_department(se_dept)

# Teachers
teacher1 = Teacher("Arsalan Ahmad", "arsalan@uni.edu", "Male", 1, "T001", "CS")
teacher2 = Teacher("Raza Sultan", "raza@uni.edu", "Male", 2, "T002", "IT")

university.hire_teacher(cs_dept, teacher1)
university.hire_teacher(it_dept, teacher2)

# Students
student1 = Student("Ayyan", "ayyan@student.edu", "Male", 101, 160, 2)
student2 = Student("Ahmad", "ahmad@student.edu", "Male", 102, 161, 2)
student3 = Student("Ali", "ali@student.edu", "Male", 103, 162, 2)

university.register_student(cs_dept, student1)
university.register_student(it_dept, student2)
university.register_student(se_dept, student3)

# Courses
course1 = Course("CS101", "Introduction to CS", 3, teacher1)
course2 = Course("IT202", "Network Fundamentals", 3, teacher2)
course3 = Course("SE303", "Software Engineering", 3, teacher1)

university.add_course(cs_dept, course1)
university.add_course(it_dept, course2)
university.add_course(se_dept, course3)

# Assign Courses to Teachers
teacher1.assigned_courses_list.append(course1)
teacher1.assigned_courses_list.append(course3)
teacher2.assigned_courses_list.append(course2)

# Enroll Students in Courses
university.enroll_student_in_course(student1, course1)
university.enroll_student_in_course(student2, course2)
university.enroll_student_in_course(student3, course3)

#  Grades
teacher1.assign_grade(student1, course1, "A")
teacher2.assign_grade(student2, course2, "B+")
teacher1.assign_grade(student3, course3, "A-")


users = [teacher1, teacher2, student1, student2, student3]

for user in users:
    user.generate_report()

# Show course summaries
course1.show_summary()
course2.show_summary()
course3.show_summary()
