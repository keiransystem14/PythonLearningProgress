print("Weclome to Missing: A Detective's Mystery")

# Detective asking Apurva's friends for a list of rooms inside Mr Apurva's Mansion

print("Detective Fetchard enters Apurva's Mansion")

Room = input("Give me a room to ivestigate for clues inside Mr Apurva's Mansion?\n")

print(f"Detective Fetchard is investigating the {Room} inside Apurva's Mansion....")

clue_found = input(f"Did you find the clues in the {Room}  yes or no?\n").lower()

if clue_found == "yes":
    print("Continue the investigating.......")

    #Interview the suspects of this cause 
    identify = input("Did you identify the suspects based on the clues given?\n")

    if identify == "yes":
        suspects = input("Please List names of the suspects you identified?\n")

        list_suspects = suspects.split()
        print(list_suspects)
        
    
else:
    print("End Investigation")

# Find the suspects





