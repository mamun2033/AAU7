# Dictionary Inversion Program on Student Course Enrollment
# This program takes a dictionary associating students with their courses 
# and inverses it to map courses with the students that are enrolled in the course.

def invert_dictionary(student_courses):
    """
    Inverts a student-to-courses dictionary into a courses-to-students dictionary.
    
    Parameters:
    student_courses (dict): A dictionary where keys are student identifiers 
                           and values are lists of course codes
    
    Returns:
    dict: An inverted dictionary where keys are course codes and values are 
          lists of students enrolled in each course
    """
    # Initialize an empty dictionary to store the inverted mapping
    inverted_dict = {}
    
    # Iterate through each student and their courses
    for student, courses in student_courses.items():
        # For each course the student is enrolled in
        for course in courses:
            # Check if this course is already a key in the inverted dictionary
            if course not in inverted_dict:
                # If not, create a new list with this student as the first entry
                inverted_dict[course] = [student]
            else:
                # If the course key exists, append the student to the existing list
                inverted_dict[course].append(student)
    
    return inverted_dict


def print_dictionary(dictionary, title):
    """
    Prints a dictionary in a formatted, readable manner.
    
    Parameters:
    dictionary (dict): The dictionary to print
    title (str): A descriptive title for the dictionary
    """
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)
    for key, value in dictionary.items():
        print(f"{key}: {value}")
    print("=" * 70)


# Main Program Execution
if __name__ == "__main__":
    
    # Original dictionary: mapping students to their enrolled courses
    original_dictionary = {
        'Stud1': ['CS1101', 'CS2402', 'CS2001'],
        'Stud2': ['CS2402', 'CS2001', 'CS1102']
    }
    
    # Display the original dictionary
    print_dictionary(original_dictionary, "ORIGINAL DICTIONARY: Students to Courses")
    
    # Invoke the inversion function
    inverted_dictionary = invert_dictionary(original_dictionary)
    
    # Display the inverted dictionary
    print_dictionary(inverted_dictionary, "INVERTED DICTIONARY: Courses to Students")
    
    # Additional functionality: Display enrollment statistics
    print("\n" + "=" * 70)
    print("ENROLLMENT STATISTICS")
    print("=" * 70)
    for course in sorted(inverted_dictionary.keys()):
        num_students = len(inverted_dictionary[course])
        students = ', '.join(inverted_dictionary[course])
        print(f"{course}: {num_students} student(s) - {students}")
    print("=" * 70)
