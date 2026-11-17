import random
choices=["rock" , "paper" , "scissors"]

while True:
    user_score=0
    computer_score=0
    n= int(input("how many rounds do you want to play?"))

    for i in range(n):
        print("round",i+1)

        user=input("choose rock,paper,or scissors:").lower().strip()

        if user not in choices:
            print("invalid choice!")
            continue

        computer=random.choice(choices)
        print("computer chose:",computer)

        if user==computer:
            print("it is a tie")

        elif(user=="rock" and computer=="scissors") or\
            (user=="paper" and computer=="rock") or\
            (user=="scissors" and computer=="paper"):
            print("you win this round")
            user_score+=1

        else:
            print("computer win this round")
            computer_score+=1

        print("------------------------------")

    print("your score:", user_score)
    print("computer score:", computer_score)

    if user_score>computer_score:
        print("you won the game")
        break
    
    elif user_score<computer_score:
        print("computer won the game")
        break
    
    else:
        print("the game is a tie")

        again=input("do you want to play again? (yes/no):").lower().strip()
    if again=="yes":
            print("starting a new game")
            continue
    else:
        print("game over. goodby")
        break
