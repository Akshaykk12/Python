"""
Raj wants to know the maximum marks scored by him in each semester. The 
mark should be between 0 to 100 ,if it goes beyond the range display “You
have entered invalid mark.”
Sample Input 1:
Enter no of semester:3
Enter no of subjects in 1 semester:3
Enter no of subjects in 2 semester:4
Enter no of subjects in 3 semester:2
Marks obtained in semester 1:506070
Marks obtained in semester 2:90987667
Marks obtained in semester 3:8976
Sample Output 1:
Maximum mark in 1 semester:70
Maximum mark in 2 semester:98
Maximum mark in 3 semester:89
"""
def find_max_marks():
    num_semesters = int(input("Enter number of semesters: "))
    
    for i in range(num_semesters):
        num_subjects = int(input(f"Enter number of subjects in semester {i+1}: "))
        marks = []
        
        for j in range(num_subjects):
            mark = int(input(f"Enter marks obtained in subject {j+1} of semester {i+1}: "))
            
            if mark < 0 or mark > 100:
                print("You have entered an invalid mark.")
                return  
            else:
                marks.append(mark)
        
        if marks:  
            print(f"Maximum mark in semester {i+1}: {max(marks)}")

find_max_marks()
