# app.py

def calculate_result(marks_obtained, total_marks):
    """
    Calculate percentage and result based on marks.
    """

    if total_marks <= 0:
        raise ValueError("Total marks must be greater than zero.")

    if marks_obtained < 0 or marks_obtained > total_marks:
        raise ValueError("Marks obtained must be between 0 and total marks.")

    percentage = (marks_obtained / total_marks) * 100

    result = "PASS" if percentage >= 40 else "FAIL"

    return percentage, result


if __name__ == "__main__":

    student_name = "Student001"
    exam_name = "DevOps Assessment"

    total_marks = 100
    marks_obtained = 85

    percentage, result = calculate_result(
        marks_obtained,
        total_marks
    )

    print("======================================")
    print("       ONLINE EXAMINATION")
    print("======================================")

    print(f"Student Name   : {student_name}")
    print(f"Exam           : {exam_name}")
    print(f"Total Marks    : {total_marks}")
    print(f"Marks Obtained : {marks_obtained}")
    print(f"Percentage     : {percentage:.2f}%")
    print(f"Result         : {result}")

    print("======================================")
