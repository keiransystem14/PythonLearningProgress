print("\nWeclome to Missing: A Detective's Mystery\n")

# Detective asking the user to respond the name of person that went missing

person = input("\nWho's the missing person?\n")

# Detective asked for the location in which the disapperance took place.

location = input(f"\nGive me a the location of where {person} is missing \n")

# Detective Fetchard enteres the specified location. 

print(f"\nDetective Fetchard enters the {location} and is currently investigating....... \n")

#Prompt to find out if there's any clues

clue_found = input(f"\nDid you find the clues in the {location} yes or no?\n").lower()

if clue_found == "yes":
    print("\nContinue investigating.......\n")

    #Find out the suspects based on those clues.
    find_suspect = input("\nQuestion: Did you identify the suspects based on the clues given? (yes or no) \n")

    if find_suspect == "yes":

        #Asking for a name of a suspect that is identified

        suspect = input("\nPlease list a name that you see as a suspect? (yes or no)\n")

        #Detective Fetchard is now interviewing the suspect with a few questions.

        print(f"\nDetective Fetchard interviewing {suspect} now....")

        alibi = input(f"\nQuestion: During the time {person} went missing, were you in a location where you can provide proof or witnesses to confirm your whereabouts? (yes or no)\n")
        activities = input(f"\nQuestion: What were you doing around the time {person} disappeared\n")
        previous_incidents = input(f"\nQuestion: Have you had any previous incidents and altercations between yourself and {person}? (yes or no)\n")
        
        #Checking if the answers the suspect is giving matches with the conditions to verify if they are a suspect or not.

        if alibi.lower() == "yes" and previous_incidents.lower() == "no":
            print("\nBased on the interview with the suspect.", suspect + ",", "they are most probably involved.\n" )
        elif alibi.lower == "no":
            print("\nBased on the interview with the suspect", suspect + ",", "It raises huge suspicion.\n")
        elif previous_incidents.lower() == "yes":
            print("\nBased on the interview with the suspect", suspect + ",", "This person is most likely a suspect\n")
        elif activities.lower() == "killed":
            print("\nBased on the interview with the suspect", suspect + ",", "Likely a suspect who's involved in harming Mr Keiran\n")
        elif activities.lower() == "lying" or activities.lower() == "hiding":
            print("\nBased on the interview with the suspect", suspect + ",", "This person seems to be hiding something.....\n" )
        else:
            print(f"\n{suspect} is not a suspect and therefore investigaton ends.\n") 
    else:
        print("\nConclude the Investigation\n")   
else:
    print("End of Investigation: No clues found, investigation inconclusive\n")







