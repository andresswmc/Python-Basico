puntaje_estudiantes = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
grados_estudiantes = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in puntaje_estudiantes:
    score = puntaje_estudiantes[student]
    if score > 90:
        grados_estudiantes[student] = "Sobresaliente"
    elif score > 80:
        grados_estudiantes[student] = "Supera las expectativas"
    elif score > 70:
        grados_estudiantes[student] = "Aceptable"
    elif score < 70:
        grados_estudiantes[student] = "Inaceptable"

# 🚨 Don't change the code below 👇
print(grados_estudiantes)