class Student:
    def _init_(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def display(self):
        print(f"Roll No: {self.roll}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class StudentManager:
    def _init_(self):
        self.students = []

    # Add Student
    def add_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        student = Student(roll, name, age)
        self.students.append(student)
        print("Student Added Successfully!")

    # Search Student
    def search_student(self):
        roll = input("Enter Roll No to Search: ")

        for student in self.students:
            if student.roll == roll:
                student.display()
                return

        print("Student Not Found!")

    # Update Student
    def update_student(self):
        roll = input("Enter Roll No to Update: ")

        for student in self.students:
            if student.roll == roll:
                student.name = input("New Name: ")
                student.age = input("New Age: ")
                print("Record Updated!")
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):
        roll = input("Enter Roll No to Delete: ")

        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print("Record Deleted!")
                return

        print("Student Not Found!")

    # Show All Students
    def show_all(self):
        if len(self.students) == 0:
            print("No Records Found")
        else:
            for student in self.students:
                student.display()
                print("-----------------")


manager = StudentManager()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.search_student()

    elif choice == "3":
        manager.update_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        manager.show_all()

    elif choice == "6":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")