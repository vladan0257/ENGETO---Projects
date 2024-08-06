"""
bullsAndCows_0.2.py: druhá verze druhého projektu do Engeto Online Python Akademie
author: Vladan Pivovarnik
email: v.pivovarnik@seznam.cz
discord username: vladan0257
"""

import random

def generateNo(digitsLength=4):
    '''
    Generate secret random number with non-repeating digits, which is to be checked against user typed-in number.
    Default length is 4 digits. Zero at first position is prohibited.

    Args:
        digitsLength (int): Set desirable length of the secret number. Place number between 1 and 10 to get a meanigful output. 
    '''
    numbersPool = list(range(10))
    secretNo = random.sample(numbersPool, digitsLength)
    secretNo[0] == random.choice([no for no in numbersPool if no not in secretNo]) if secretNo[0] == 0 else secretNo[0] == secretNo[0]
    return ''.join([str(no) for no in secretNo])

def isValidNo(userNo, secretNo):
    '''
    Check players'input and eventally call for new attempt, when it is not all numeric, contains duplicates or begins with 0.

    Args:
        userNo (str): User input.
        secretNo (str): 
    '''
    correctLength = isUnique = firstNotZero = allNum = True

    if len(secretNo) != len(userNo):
        print(f'I\'am missing {len((secretNo))} digits in your number.')
        correctLength = False

    if len(set(userNo)) != len(userNo):
        print('Your number contains some duplicates.')
        isUnique = False

    if userNo[0] == '0':
        print('Zero at first position!')
        firstNotZero = False

    if not userNo.isdigit():
        print('Your input is not purely numeric.')
        allNum = False

    if correctLength and isUnique and firstNotZero and allNum:
        return True
    
    else:
        return False

def separator(stringsList):
    '''
    Return array of asterisks for better oreintation and readability.  

    Args:
        stringsList (list): Introductory text (variable introTxt) is divided into several sections. The function takes into 
        consideration length of each individual section and returns a string of asterisks of length of the longest one 
        contained in the list, so the text and everything that follows is visually coherent and causes no distraction to the 
        reader. 
    '''
    return '-' * len(max(stringsList, key=len))

def printIntro(stringsList, separator):
    '''
    Show introductory text.

    Args:
        stringsList (list): Introductory text (variable introTxt) is divided into several sections. The function takes into 
        consideration length of each individual section and returns a string of asterisks of length of the longest one 
        contained in the list, so the text and everything that follows is visually coherent and causes no distraction to the 
        reader.  
        separator (str): Separates the text for better oreintation and readability using an array of asterisks.
 
    '''
    print(stringsList[0], stringsList[1], separator, stringsList[2], stringsList[3], separator, stringsList[4], sep='\n')

def processStats(userNo, secretNo):
    '''
    Compare a user number with randomly generated number, which is to be revealed. For each number match a player gets 
    1 point for 'cows'. When the player hits correct number and at the same time its position, 1 point goes for 'bulls'. 
    The game ends, when player collects 4 points for 'bulls'.

    Example: secret no is 5793, players' input is 1398: The player gets 1 point for cows, because both numbers contain no 3
    and 1 point for bulls, because number 9 in players' input is also present within the secret number and moreover it is on 
    the same position.

    Args:
        userNo (str): User typed number.
        secretNo (str): The number, which is to be revealed.
    '''
    results = {'bulls': sum(userNo[i] == secretNo[i] for i in range(len(userNo))), 'cows': sum(ch in secretNo for ch in userNo)}
    results['cows'] = results['cows'] - results['bulls']
    return results

def showStats(statsDict):
    '''
    Print each round results.

    Args:
        statsDict (dict): A dictionary with a numeric representation of players' progress in the game. Players' aim is to get
        4 points in as few rounds as possible for the 'bulls' key, which is indication that the whole number has been revealed.
    '''
    rawTxt = '{} bull{}, {} cow{}'
    print(rawTxt.format(statsDict['bulls'], 's' if statsDict['bulls'] != 1 else '', statsDict['cows'], 's' if statsDict['cows'] != 1 else ''))

def showEvaluation(round, separator):
    '''
    Show how many rounds a player needed in order to get the right number and follow it with a verbal interpretation of the actual result.

    Args:
        round (int): A rounds'counter. Initiate with 0 and add 1 each time the player is urged to put his number, which means that even
        not entirely numeric input is treated as a valid attempt. 
        separator (str): Dividing annoucment containing number of rounds and verbal interpretation for better readibility.
    '''
    first, second, third, fourth = list(range(1, 4)), list(range(4, 6)), list(range(6, 8)), list(range(8, 100))   
    stats = {'That\'s impressive!': first, 'That\'s satisfying.': second, 'Not great, not terrible.': third, 'Get some rest, mate!': fourth}
    statement = [key for key, val in stats.items() if round in val]
    print(f'Correct, you\'ve guessed the right number in \n{round} guesses!', separator, statement[0], sep='\n')


def main():

    secretNo = generateNo()
    # print(secretNo)
    introTxt = ['', 'Hi there!', f'I\'ve generated a random {len(secretNo)} digit number for you.', 
    'Let\'s play a bulls and cows game.', 'Enter a number:']
    sep = separator(introTxt)
    printIntro(introTxt, sep)

    turn = 0
    
    while True:
        
        print(sep)
        userNo = input('>>> ')
        turn += 1

        if isValidNo(userNo, secretNo):
            doStats = processStats(userNo, secretNo)

            if userNo != secretNo:
                showStats(doStats)

            else:
                break

    showEvaluation(turn, sep)

if __name__ == '__main__':
    main()
