answer1 = input("Did the player lose consciousness or are they unresponsive? ")
if answer1 == "y" :
    print("Player is disqualified due to risk of concussion.")
else:
    answer2 = input("Does player display any disorientation or inability to repond appropriately to questions?")

    if answer2 == "y" :
        print("Player is disqualified due to risk of concussion.")

    else:
        answer3 = input("Does the player display any signs of retrograde or anterograde amnesia?")
        if answer3 == "y" :
            print("Player is disqualified due to risk of concussion.")

        else:
            answer4 = input("Does the player display any new or persistent symptoms?")
        if answer4 == "y" :
            print("Player is disqualified due to risk of concussion.")

        else:
            answer5 = input("Does the player display any abnormal neurological finding?")
        if answer5 == "y" :
            print("Player is disqualified due to risk of concussion.")

        else:
            answer6 = input("Does the player display progressive, persistent or worsening symptoms?")
        if answer5 == "y" :
            print("Player is disqualified due to risk of concussion.")

        else:
            print("Move on to the visual concussion test")
