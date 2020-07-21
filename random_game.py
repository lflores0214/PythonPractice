from random import randint
import sys

# generate a number 1 - 10

# input from user

# check if input is a number 1 - 10

# check if user guessed the right number

# otherwise ask again


# number = randint(int(sys.argv[1]), int(sys.argv[2]))
# while True:
#     try:
#         guess = int(
#             input(f"Guess a number between {sys.argv[1]} and {sys.argv[2]}: "))
#         if guess > int(sys.argv[2]) or guess <= int(sys.argv[1]):
#             print(
#                 f"please choose a number between {sys.argv[1]} and {sys.argv[2]}")
#             continue
#         elif guess != number:
#             continue
#         elif guess == number:
#             print("Correct!")
#             break
#     except ValueError:
#         print("please input a number")
#         continue

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you got it!')
            return True
    else:
        print('enter a number between 1 and 10')
        return False
if __name__ == '__main__':
    unittest.main()
    answer = randint(1,10)

    while True:
        try:
            guess = int(input('guess a number between 1 and 10: '))
            if (run_guess(guess,answer)):
                break
        except ValueError:
            print('please enter a number')
            continue