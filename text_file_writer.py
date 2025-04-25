with open("mylife.txt", 'w') as userFile:
    user_input = 'y'
    
    while user_input == 'y':
        user_life = input("Enter line: ")
        userFile.write(user_life + "\n")
        
        while True:
            try:            
                add_line = input("Do you want to add more lines? (y/n): ").lower()
                
                if add_line == 'y' or add_line == 'n':
                    break
                else:
                    raise ValueError
            
            except ValueError:
                print("Your answer should be 'y' or 'n' only.")
                
        if add_line == 'n':
            break
        
userFile.close()