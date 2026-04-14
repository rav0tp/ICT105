session3 # type: ignore

courses = ["Physics I", "Calculus I", "Biology I", "History I", "Microeconomics"]

print(courses)
print(sorted(courses))
print(sorted(courses, reverse=True))

courses.reverse()
print(courses)
courses.reverse()
print(courses)

courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

# Replace a course
courses[0] = "Chemistry I"
print("Withdrawn: Physics I")
print("Added: Chemistry I")
print(courses)

# Add 3 courses
courses.insert(0, "Calculus II")
courses.insert(2, "English I")
courses.append("Psychology I")
print(courses)

# Remove 4 with pop()
print("Removed:", courses.pop(0))
print("Removed:", courses.pop(1))
print("Removed:", courses.pop(2))
print("Removed:", courses.pop(3))
print(courses)

# Tuples
tuples = [(1,"Physics I"),(2,"Calculus I"),(3,"Biology I")]
names = []
for t in tuples:
    names.append(t[1])
print(names)