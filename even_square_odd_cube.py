integersFile = open("integers.txt", "r")
doubleFile = open("double.txt", "w") 
tripleFile = open("triple.txt", "w") 

for line in integersFile:
    line = line.strip() 
    numbers = line.split() 

    for number in numbers:
        num = int(number) 

        if num % 2 == 0: 
            doubleFile.write(str(num ** 2) + "\n")  
        else:  
            tripleFile.write(str(num ** 3) + "\n")  

integersFile.close()
doubleFile.close()
tripleFile.close()