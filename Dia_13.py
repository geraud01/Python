print ("Exam Grade Calculator")
print ()
print ("Name of exam:")
print ()
total_score = int (input ("Max. Total score:"))
letter_grade = int (input("Enter your exam grade:"))

score = float (letter_grade / total_score)
final_number = round (score, 2)
final_perce = round(float(letter_grade / total_score)*100, 2)
print ("You got", final_perce,"%")

if letter_grade >= 90 and letter_grade <= 100:
  print ("You got an A+")
elif letter_grade >= 80 and letter_grade <= 89:
  print ("You got a A")
elif letter_grade >= 70 and letter_grade <= 79:
  print ("You got a B")
elif letter_grade >= 60 and letter_grade <= 69:
  print ("You got a C")
elif letter_grade >= 50 and letter_grade <= 59:
  print ("You got a D")
elif letter_grade <= 49:
  print ("You got an U")    
else:
  print ("Invalid grade")