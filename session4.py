session4

departments = [[1,"Computer Science"],[2,"Mathematics"],[3,"Physics"],
               [4,"Chemistry"],[5,"Biology"]]

while True:
    user_input = input("Enter Course ID (0 to quit): ")
    if user_input == "0" or user_input == "quit":
        print("Exiting.")
        break
    num = int(user_input)
    found = False
    for item in departments:
        if item[0] == num:
            print("Department:", item[1])
            found = True
            break
    if not found:
        print("Course not found.")

courses = [
    [1,"Intro to Programming","Computer Science","None"],
    [2,"Calculus I","Mathematics","None"],
    [3,"Physics I","Physics","None"]
]

while True:
    user_input = input("Enter Course ID (0 to quit): ")
    if user_input == "0":
        break
    num = int(user_input)
    found = False
    for row in courses:
        if row[0] == num:
            print("Name:", row[1])
            print("Department:", row[2])
            print("Prerequisites:", row[3])
            found = True
            break
    if not found:
        print("Course not found.")