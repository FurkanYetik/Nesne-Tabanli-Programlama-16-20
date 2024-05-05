import csv

# Create the CSV file
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['student_id', 'username', 'password'])
    students = [
        {'1': 'student1', 'Furkan': 'student1', '12345678': 'password1'},
        {'2': 'student2', 'Ilkan': 'student2', '12345678': 'password2'},
        {'3': 'student1', 'Emir': 'student1', '12345678': 'password1'},
        {'4': 'student2', 'Cagri': 'student2', '12345678': 'password2'},
        # add more students as needed
    ]
    writer.writerows(student for student in students)

# Read the student data from the file
student_ids = {}
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        student_id, username, password = row
        student_ids[student_id] = {"username": username, "password": password}