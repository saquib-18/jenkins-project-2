with open("report.txt", "w") as file:
    file.write("Application Build Report\n")
    file.write("=======================\n")
    file.write("Build Status: SUCCESS\n")
    file.write("Test Status: PASSED\n")
    file.write("Deployment Status: SUCCESS\n")

print("Report generated successfully.")
