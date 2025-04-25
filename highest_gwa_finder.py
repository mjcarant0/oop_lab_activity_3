gwaFile = open("gwa.txt", "r")

highest_gwa = 0
highest_student = ""

for line in gwaFile:
    student, gwa = line.strip().split(',')
    
    gwa = float(gwa)
    
    if gwa > highest_gwa:
        highest_gwa = gwa
        highest_student = student

print(f"The student with highest GWA is: {highest_student}")
print(f"GWA: {highest_gwa}")

gwaFile.close()