import random
def projectgame():
     user_choice=input("Enter your choice here \n stone \n paper \n scissors \n").lower()

     computer=random.randrange(1,4)

     if computer==1:
          computer_choice="stone"
     elif computer==2:
          computer_choice="paper"
     else:
          computer_choice="scissors"

     print("computer chose:",computer_choice)

     if user_choice==computer_choice:
          print("It's a Tie.\n")
     elif user_choice=="stone" and computer_choice=="scissors":
          print("you win!.") 
     elif user_choice=="paper" and computer_choice=="stone":
          print("you win!.")
     elif user_choice=="paper" and computer_choice=="scissors":
          print("computer wins!.")
     elif user_choice=="scissors" and computer_choice=="stone":
          print("computer wins!.")
     elif user_choice=="scissors" and computer_choice=="paper":
          print("you win!.")
     else:
          print("INVALID CHOICE \n TRY AGAIN")


projectgame()




           
          