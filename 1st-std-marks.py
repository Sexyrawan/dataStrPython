""" 
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message. """

student_mark = {
    'anuj': 95,
    'rahul': 78,
    'nitin': 80,
    'shasvat': 66,
    'bhanu': 99,   
}

print("enter the name of the student Whose number do you want to find out?")
user_inp = input("Student name:").lower()
if user_inp in student_mark:
    print(f"{user_inp.title()} scored: {student_mark[user_inp]} marks")
else:
    print("❌ wrong input \n❌ Student not Found!")