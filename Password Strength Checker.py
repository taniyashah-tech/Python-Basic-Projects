'''7. Password Strength Checker 
Intermediate 
Concepts: Conditions, loops, functions, strings 
Requirements 
• Accept a password from the user. 
• Check its length. 
• Check for uppercase and lowercase letters. 
• Check for digits and special characters. 
• Classify it as weak, medium, or strong according to your defined rules. 
Bonus: Display suggestions to improve a weak password.'''

def checker():
  password = input("Enter password: ")
  
  length = len(password)
  
  upper = 0
  lower = 0
  digit = 0
  special = 0
  
  for ch in password:
      if 'A' <= ch <= 'Z':
          upper += 1
      elif 'a' <= ch <= 'z':
          lower += 1
      elif '0' <= ch <= '9':
          digit += 1
      else:
          special += 1
  
  score = 0
  
  if length >= 8:
      score += 1
  if upper > 0:
      score += 1
  if lower > 0:
      score += 1
  if digit > 0:
      score += 1
  if special > 0:
      score += 1
  
  print("\nPassword Analysis")
  print("Length:", length)
  print("Uppercase Letters:", upper)
  print("Lowercase Letters:", lower)
  print("Digits:", digit)
  print("Special Characters:", special)
  
  if score <= 2:
      print("Strength: Weak")
      
      print("\nSuggestions:")
      if length < 8:
          print("- Make password at least 8 characters long")
      if upper == 0:
          print("- Add uppercase letters")
      if lower == 0:
          print("- Add lowercase letters")
      if digit == 0:
          print("- Add digits")
      if special == 0:
          print("- Add special characters")
      elif score <= 4:
          print("Strength: Medium")
      else:
          print("Strength: Strong")

checker()
