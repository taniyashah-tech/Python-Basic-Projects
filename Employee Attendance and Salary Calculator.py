'''8. Employee Attendance and Salary Calculator 
Intermediate 
Concepts: Conditions, loops, functions, dictionaries 
Requirements 
• Enter employee details and days present. 
• Calculate attendance percentage. 
• Calculate salary based on days worked. 
• Apply a bonus or deduction according to attendance rules. 
• Generate an employee summary. '''

def employee_attendance_salary_calculator():
  def calculate_attendance(days_present, total_days):
      return (days_present / total_days) * 100
  
  
  def calculate_salary(salary_per_day, days_present):
      return salary_per_day * days_present
  
  
  def employee_summary(emp):
      attendance = calculate_attendance(
          emp["days_present"], emp["total_days"]
      )
  
      salary = calculate_salary(
          emp["salary_per_day"], emp["days_present"]
      )
  
      bonus = 0
      deduction = 0
  
      if attendance >= 90:
          bonus = salary * 0.10
      elif attendance < 75:
          deduction = salary * 0.05
  
      final_salary = salary + bonus - deduction
  
      print("\n===== Employee Summary =====")
      print("ID :", emp["id"])
      print("Name :", emp["name"])
      print("Days Present :", emp["days_present"])
      print("Attendance % :", attendance)
      print("Basic Salary :", salary)
      print("Bonus :", bonus)
      print("Deduction :", deduction)
      print("Final Salary :", final_salary)
  
  
  employee = {}
  
  employee["id"] = input("Enter Employee ID: ")
  employee["name"] = input("Enter Employee Name: ")
  employee["total_days"] = int(input("Enter Total Working Days: "))
  employee["days_present"] = int(input("Enter Days Present: "))
  employee["salary_per_day"] = float(input("Enter Salary Per Day: "))
  
  employee_summary(employee)

employee_attendance_salary_calculator()
