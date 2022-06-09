# A Game of Rock Paper Scissors
# Made By M Samson Badding
import  random

def rockPaperScissors(personWin, compWin, work):

    while True:
        print()
        personinput = input("Enter Rock / Paper / Scissor or 0 to exit: ").lower()
        if personinput not in work:
            print('Value not recognized')
            continue

        randomNum = random.randint(0, 2)
        compuGuess = work[randomNum]

        if (personinput == 'rock' and compuGuess == 'scissors') or (personinput == 'paper' and compuGuess == 'rock') or (personinput == 'scissors' and compuGuess == 'paper'):
            print('Computer: ', compuGuess)
            print('You win')
            personWin += 1
        elif (personinput == 'rock' and compuGuess == 'rock') or (personinput == 'paper' and compuGuess == 'paper') or (personinput == 'scissors' and compuGuess == 'scissors'):
            print('Computer: ', compuGuess)
            print('No one wins point')
        else:
            print('Computer: ', compuGuess)
            print('You Lost')
            compWin += 1

        if personinput == '0':
            print()
            print('Thank you for Playing')
            break

    print('Your score: ', personWin)
    print('Computer score: ', compWin)

if __name__ == '__main__':
    print('WELCOME TO A GAME OF ROCK / PAPER / SCISSORS')
    # To count the points won by the players (user and computer)
    userWin = 0
    machineWin = 0

    options = ['rock', 'paper', 'scissor', '0']

    rockPaperScissors(userWin, machineWin, options)


