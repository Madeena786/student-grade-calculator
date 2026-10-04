print("***********STUDENT GRADE CALCULATOR***********")
name=input("Enter student name:")
while True:
    python=int(input("Enter Python marks:"))
    if 0<=python<=100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")
while True:
    sql=int(input("Enter SQL marks:"))
    if 0<=sql<=100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")
while True:
    html=int(input("Enter HTML marks:"))
    if 0<=html<=100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")
while True:
    css=int(input("Enter CSS marks:"))
    if 0<=css<=100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")
while True:
    javascript=int(input("Enter JavaScript marks:"))
    if 0<=javascript<=100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")
total = python+sql+html+css+javascript
percentage = total / 5
if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B"
elif percentage>=60:
    grade="C"
elif percentage>=50:
    grade="D"
elif percentage>=40:
    grade="E"
else:
    grade="F"
print("\n********STUDENT RESULT*********")
print("Student Name:",name)
print("Python:", python)
print("SQL:", sql)
print("HTML:", html)
print("CSS:", css)
print("JavaScript:", javascript)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
