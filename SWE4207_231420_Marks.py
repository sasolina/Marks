global marksA, user
def quitA():
    quitB = input('Enter [done] if you wish to quit or [No] redo: ')
    if quitB == 'done' or quitB == 'Done':
        exit()
    elif quitB == 'no' or quitB == 'No':
        marker()
    else:
        print ('Invalid input, please enter yes or no ')
        quitA()

        
grades = []

counter = 0
def marker():
    for i in range(3):
        while True:
            try:
                grade = int(input(f"Enter grade {i + 1}: "))
                grades.append(grade)
                break
            except ValueError:
                print("Please enter a valid numeric grade.")

    # Calculate the largest, smallest, and average grades
    if grades:
        largest_grade = max(grades)
        smallest_grade = min(grades)
        average_grade = sum(grades) / len(grades)
        int_num = [largest_grade, smallest_grade, average_grade]
        
        print("Largest grade:", int_num[0])
        print("Smallest grade:", int_num[1])
        print("Average grade:", int_num[2])
        quitA()    
    else:
        print("No grades entered.")
marker()