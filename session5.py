session5  # type: ignore

# Task 1: Student Course Enrollment

course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"],
    1005: ["BIO101", "HIST101"],
}

for student_id, courses in course_enrollments.items():
    print(f"Student ID: {student_id} | Courses: {courses}")

    # Task 2: Class Schedule by Department

departments = {
    "Computer Science": [("Computer Science", "CS101", "Intro to Computer Science"),
                         ("Computer Science", "CS202", "Data Structures and Algorithms")],
    "Mathematics":      [("Mathematics", "MATH101", "Calculus I"),
                         ("Mathematics", "MATH102", "Calculus II")],
    "Physics":          [("Physics", "PHY101", "General Physics I")],
}

for dept, courses in departments.items():
    print(f"\n{dept}:")
    for course in courses:
        print(f"  {course}")

        