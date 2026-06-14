#Michael Gordon
#CIS261
#WK10 VIBE Coding
#Student Grade Calculator

students = []
FILE_NAME = "student_grades.txt"

def calculate_average(test1, test2, test3):
    """Calculate the average of three test scores."""
    return (test1 + test2 + test3) / 3

def calculate_grade(average):
    """Calculate letter grade based on average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def get_valid_float(prompt):
    """Get valid float input from user."""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_student():
    """Add a new student record."""
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return
    
    student_id = input("Enter student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    
    # Check if student ID already exists
    for student in students:
        if student['id'].lower() == student_id.lower():
            print("Student ID already exists.")
            return
    
    test1 = get_valid_float("Enter Test 1 score (0-100): ")
    test2 = get_valid_float("Enter Test 2 score (0-100): ")
    test3 = get_valid_float("Enter Test 3 score (0-100): ")
    
    average = calculate_average(test1, test2, test3)
    grade = calculate_grade(average)
    
    student = {
        'name': name,
        'id': student_id,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'average': average,
        'grade': grade
    }
    
    students.append(student)
    print(f"\nStudent '{name}' added successfully!")

def display_all_students():
    """Display all students in a formatted table."""
    if not students:
        print("\nNo students in the system.")
        return
    
    print("\n" + "="*110)
    print(f"{'Name':<20} {'ID':<12} {'Test1':<8} {'Test2':<8} {'Test3':<8} {'Average':<10} {'Grade':<6}")
    print("="*110)
    
    for student in students:
        print(f"{student['name']:<20} {student['id']:<12} "
              f"{student['test1']:<8.2f} {student['test2']:<8.2f} {student['test3']:<8.2f} "
              f"{student['average']:<10.2f} {student['grade']:<6}")
    
    print("="*110)

def calculate_statistics():
    """Calculate and display class statistics."""
    if not students:
        print("\nNo students to calculate statistics for.")
        return
    
    averages = [student['average'] for student in students]
    highest = max(averages)
    lowest = min(averages)
    class_average = sum(averages) / len(averages)
    
    # Find students with highest and lowest averages
    highest_student = next(s for s in students if s['average'] == highest)
    lowest_student = next(s for s in students if s['average'] == lowest)
    
    print("\n" + "="*60)
    print("CLASS STATISTICS")
    print("="*60)
    print(f"Total Students: {len(students)}")
    print(f"Highest Average: {highest:.2f} ({highest_student['name']})")
    print(f"Lowest Average: {lowest:.2f} ({lowest_student['name']})")
    print(f"Class Average: {class_average:.2f}")
    print("="*60)

def search_student():
    """Search for a student by name (case-insensitive)."""
    if not students:
        print("\nNo students in the system.")
        return
    
    search_name = input("\nEnter student name to search: ").strip().lower()
    
    found_students = [s for s in students if search_name in s['name'].lower()]
    
    if not found_students:
        print(f"No students found with '{search_name}' in their name.")
        return
    
    print("\n" + "="*110)
    print(f"{'Name':<20} {'ID':<12} {'Test1':<8} {'Test2':<8} {'Test3':<8} {'Average':<10} {'Grade':<6}")
    print("="*110)
    
    for student in found_students:
        print(f"{student['name']:<20} {student['id']:<12} "
              f"{student['test1']:<8.2f} {student['test2']:<8.2f} {student['test3']:<8.2f} "
              f"{student['average']:<10.2f} {student['grade']:<6}")
    
    print("="*110)

def save_students():
    """Save student records to file in pipe-delimited format."""
    try:
        with open(FILE_NAME, 'w') as file:
            for student in students:
                line = f"{student['name']}|{student['id']}|{student['test1']:.2f}|{student['test2']:.2f}|{student['test3']:.2f}|{student['average']:.2f}|{student['grade']}\n"
                file.write(line)
        print(f"\nStudent records saved to '{FILE_NAME}'.")
    except IOError as e:
        print(f"\nError saving file: {e}")

def load_students():
    """Load student records from file."""
    global students
    try:
        students = []
        try:
            with open(FILE_NAME, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split('|')
                        if len(parts) == 7:
                            student = {
                                'name': parts[0],
                                'id': parts[1],
                                'test1': float(parts[2]),
                                'test2': float(parts[3]),
                                'test3': float(parts[4]),
                                'average': float(parts[5]),
                                'grade': parts[6]
                            }
                            students.append(student)
                print(f"Loaded {len(students)} student records from '{FILE_NAME}'.")
        except FileNotFoundError:
            print(f"No saved file found. Starting with empty student list.")
    except Exception as e:
        print(f"Error loading file: {e}")
        students = []

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("STUDENT GRADE CALCULATOR")
    print("="*50)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Calculate Class Statistics")
    print("4. Search for Student")
    print("5. Save Records")
    print("6. Exit (or press ESC)")
    print("="*50)

def main():
    """Main program loop."""
    print("Starting Student Grade Calculator...")
    load_students()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6) or press ESC to exit: ").strip()
        
        if choice.upper() == 'ESC' or choice == '\x1b' or choice == '':
            if input("Are you sure you want to exit? (yes/no): ").strip().lower() == 'yes':
                save_students()
                print("Thank you for using Student Grade Calculator. Goodbye!")
                break
        elif choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            calculate_statistics()
        elif choice == '4':
            search_student()
        elif choice == '5':
            save_students()
        elif choice == '6':
            if input("Are you sure you want to exit? (yes/no): ").strip().lower() == 'yes':
                save_students()
                print("Thank you for using Student Grade Calculator. Goodbye!")
                break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()