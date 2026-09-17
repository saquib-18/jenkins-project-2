# generate_report.py

student_name = "Student001"
exam_name = "DevOps Assessment"

total_marks = 100
marks_obtained = 85

percentage = (marks_obtained / total_marks) * 100

result = "PASS" if percentage >= 40 else "FAIL"

print("======================================")
print("       ONLINE EXAMINATION REPORT")
print("======================================")

print(f"Student Name : {student_name}")
print(f"Exam         : {exam_name}")
print(f"Total Marks  : {total_marks}")
print(f"Marks Obtained: {marks_obtained}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")

print("======================================")

# Generate report.txt for Jenkins artifact archiving
with open("report.txt", "w") as file:
    file.write("ONLINE EXAMINATION REPORT\n")
    file.write("=========================\n")
    file.write(f"Student Name : {student_name}\n")
    file.write(f"Exam         : {exam_name}\n")
    file.write(f"Total Marks  : {total_marks}\n")
    file.write(f"Marks Obtained: {marks_obtained}\n")
    file.write(f"Percentage   : {percentage:.2f}%\n")
    file.write(f"Result       : {result}\n")

print("\nReport generated successfully.")
