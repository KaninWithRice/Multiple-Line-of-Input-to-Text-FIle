# Mohammad Mishal S. Noroña | BSCPE 1-5 | Porblem 1 Multiple Line of Text Into a Text File
# Add introduction
print("")
print("WELCOME TO THE ATTENDANCE LIST ".center(40," ") )
print("By: Mishal Noroña".center(40," ") )
# Ask for User's Input
atendance_list = "name_list.txt"
with open("Attendance.txt", "w") as attendance_list:
    while True:
        name_input = input("Enter a name: ")
        attendance_list.write(name_input + "\n")
# Ask if he/she wants to input another
        another_input = input("Do you want to enter another? y/n ")
# If y the program will ask for another name
# If n the program will end
# Prints Attendance List