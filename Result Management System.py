'''2. Student Result Management System 
Beginner 
Concepts: Conditions, loops, functions 
Requirements 
• Input marks for five subjects. 
• Calculate total, percentage, and grade. 
• Check whether the student passed or failed. 
• Validate that each mark is between 0 and 100. 
• Create functions such as calculate_total(), calculate_percentage(), and 
calculate_grade(). 
Bonus: Accept results for multiple students and calculate the class average.'''

def result():

    def calculate_total(sub1,sub2,sub3,sub4,sub5):
        return sub1+sub2+sub3+sub4+sub5

    def calculate_percentage(total):
        return total / 5

    def calculate_grade(percentage):
        if percentage >= 90 and percentage <= 100 :
            return "Grade A"
        elif percentage >= 75:
            return "Grade B"
        elif percentage >= 50:
            return "Grade C"
        elif percentage >= 30:
            return "Grade D"
        else:
            return "Grade F"
    students = int(input("Enter the number of students"))
    i = 1  
    while i <= students:
        name = input ("enter the name of student ")
        sub1 = int(input("Enter the marks of Sub1"))
        sub2 = int(input("Enter the marks of Sub2"))
        sub3 = int(input("Enter the marks of Sub3"))
        sub4 = int(input("Enter the marks of Sub4"))
        sub5 = int(input("Enter the marks of Sub5"))
        
        if (sub1<0  or sub1 > 100 or
            sub2<0  or sub2 > 100 or
            sub3<0  or sub3 > 100 or
            sub4<0  or sub4 > 100 or
            sub5<0  or sub5 > 100):
            print("Invalid Marks!")
        else:   
            total = calculate_total(sub1,sub2,sub3,sub4,sub5)
            percentage = calculate_percentage(total)
            grade = calculate_grade(percentage)
        
    
result()
