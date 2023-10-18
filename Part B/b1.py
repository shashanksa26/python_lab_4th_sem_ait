import random
n = random.randint(1, 9)
name = input('Hi, Whats your name? ')
print("Well", name, "i am thinking of a number between 1 and 100, take a guess")
guess = 0
while n != guess:
    guess = int(input())
    if guess < n:
        print("your guess is too low. Try again.")
    elif guess > n:
        print("your guess is too high. Try again.")
print("Good job, you got it!")