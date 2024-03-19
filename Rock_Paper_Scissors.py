import random
l=["rock","paper","scissor"]
print("------------------------------")
print("The game will be of 3 rounds")
print("------------------------------")
while(True):
    usercount=0
    comcount=0


    choice=int(input("""
Do you want to play the Game ....
1. YES
2. NO
    """))
    if choice==1:
        for i in range(1,4):
            user=int(input("""
1 rock
2 paper
3 scissor
            """))
            if user==1:
                userchoice="rock"
            elif user==2:
                userchoice="paper"
            elif user==3:
                user="scissor"
            comchoice=random.choice(l)

            if (comchoice==userchoice):
                print("-------------------------")
                print("Your Choice : {}".format(userchoice))
                print("-------------------------")
                print("Computer Choice : {}".format(comchoice))
                print("-------------------------")
                print("Round Draw")
                print("-------------------------")
                usercount=usercount+1
                comcount=comcount+1
            elif ((userchoice=="rock") and (comchoice=="scissor") or
                  (userchoice=="paper") and (comchoice=="rock") or
                  (userchoice=="scissor") and (comchoice=="paper")):
                print("-------------------------")
                print("Your Choice : {}".format(userchoice))
                print("-------------------------")
                print("Computer Choice : {}".format(comchoice))
                print("-------------------------")
                print("You win")
                print("-------------------------")
                usercount=usercount+1
            else:
                print("-------------------------")
                print("Your Choice : {}".format(userchoice))
                print("-------------------------")
                print("Computer Choice : {}".format(comchoice))
                print("-------------------------")
                print("Computer win")
                print("-------------------------")
                comcount=comcount+1
        if (usercount==comcount):
            print("----------------------")
            print("Your Count : {}".format(usercount))
            print("Computer Count : {}".format(comcount))
            print("----------------------")
            print("Game Draw")
            print("----------------------")
        elif (usercount > comcount):
            print("----------------------")
            print("Your Count : {}".format(usercount))
            print("Computer Count : {}".format(comcount))
            print("----------------------")
            print("You won the game")
            print("----------------------")
        else:
            print("----------------------")
            print("Your Count : {}".format(usercount))
            print("Computer Count : {}".format(comcount))
            print("----------------------")
            print("Computer won the game")
            print("----------------------")


    else:
        break