def calculate_result(marks, total):
    return (marks / total) * 100


if __name__ == "__main__":
    marks = 80
    total = 100

    percentage = calculate_result(marks, total)

    print(f"Marks: {marks}")
    print(f"Percentage: {percentage}%")
    print("Application executed successfully.")
