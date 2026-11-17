import random
words=["apple", "banana","orange","python", "computer"]
word=random.choice(words)

guessed_letters=[]
chances=6
print("welcome to hangman")

while chances>0:
    display=""

    for letter in word:
        if letter in guessed_letters:
            display+=letter+""
        else:
            display+="_"

    print("word:",display)
    if "_" not in display:
        print("congratulations! you win")
        break

    guess=input("guess a letter:").lower().strip()
    if len(guess)!=1 or not guess.isalpha():
        print("please enter only one letter")
        continue

    if guess in guessed_letters:
        print("you already guessed this letter")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("correct guess")

    else:
        chances-=1
        print("wrong guess")
        print("remaining chances:", chances)

else:
    print("you lose")
    print("the correct word was:",word)
