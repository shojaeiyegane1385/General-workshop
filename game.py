import random
print("rock , paper , scissors game")
print("------------------------------")
choices=["rock" , "paper" , "scissors"]

while True:
    user=input("choose rock , paper , scissors or exit :")

    if user=="exit":
        print("game over. goodbye!")
        break
    if user not in choices:
        print("please enter a valid choice.")
        continue

    computer=random.choices(choices)
    print("computer chose:" , computer)

    if user==computer:
        print("it is a tie!")

    elif (user=="rock" and computer=="scissors")or\
         (user=="paper" and computer=="rock")or\
         (user=="scissors" and computer=="paper"):
        print("you win")

    else:
        print("computer wins")
        print("------------------------------")