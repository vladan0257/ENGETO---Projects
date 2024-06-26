"""
bullsAndCows.py: druhý projekt do Engeto Online Python Akademie
author: Vladan Pivovarnik
email: v.pivovarnik@seznam.cz
discord username: vladan0257
"""

import random

def generateNo(digitsLength):
    '''
    Generate secret random number with non-repeating digits, which is to be checked against user typed-in number.
    Default length is 4 digits. Zero at first position is prohibited.

    Args:
        digitsLength (int): Set desirable length of the secret number. Place number between 1 and 10 to get a meanigful output. 
    '''
    numbersPool = list(range(10))
    secretNo = random.sample(numbersPool, digitsLength)
    secretNo[0] == random.choice(set(numbersPool) - set(secretNo)) if secretNo[0] == 0 else secretNo[0] == secretNo[0]
    return ''.join([str(no) for no in secretNo])

def guessNo(secretNo):
    '''
    First prompt user to type-in his number and check if his input is numerical. Then check against a randomly
    generated number and assess, how close the user input is to the secret number and return the result. 
    This above cycle repeats untill both - user and the secret number - are identical. At this point the function 
    returns how many attempts has been passed since the first input. A user non-numerical input is not counted 
    as a valid guess, therefore it is not included in the stats.

    Args:
        secretNo (int): A randomly generated unique (non-repeated figures) number, that is to be revealed.
    '''
    txt = ['',
    'Hi there!',
    f'I\'ve generated a random {len(str(secretNo))} digit number for you.', 
    'Let\'s play a bulls and cows game.',
    'Enter a number:']
    separ = '-' * len(max(txt, key=len))
    print(txt[0], txt[1], separ, txt[2], txt[3], separ, txt[4], sep='\n')

    turn = 0

    while True:
        print(separ)
        yourNo = input('>>> ')
        correctLength = isUnique = firstNotZero = allNum = True

        if len(str(secretNo)) != len(yourNo):
            print(f'We\'re missing {len(str(secretNo))} digits in your number.')
            correctLength = False
        
        if len(set(yourNo)) != len(yourNo):
            print('Your number contains some duplicates.')
            isUnique = False
        
        if yourNo[0] == '0':
            print('Zero at first position!')
            firstNotZero = False
        
        if not yourNo.isdigit():
            print('Your input is not purely numeric.')
            allNum = False

        if correctLength and isUnique and firstNotZero and allNum:
                results = {'bulls': sum(yourNo[i] == secretNo[i] for i in range(len(yourNo))), 'cows': sum(ch in secretNo for ch in yourNo)}
                rawTxt = '{} bull{}, {} cow{}'
                first, second, third, fourth = list(range(1, 4)), list(range(4, 6)), list(range(6, 8)), list(range(8, 100))   
                stats = {'Impressive!': first, 'That\'s satisfying.': second, 'Not great, not terrible.': third, 'Get some rest, mate!': fourth}

                turn += 1
                statement = [key for key, val in stats.items() if turn in val]

                if results['bulls'] != 4:
                    print(rawTxt.format(results['bulls'], 's' if results['bulls'] != 1 else '', results['cows'], 's' if results['cows'] != 1 else ''))
                    
                else: 
                    print(f'Correct, you\'ve guessed the right number in {turn} guesses!')
                    print(separ, statement[0], sep='\n')
                    break

def main():
    noLength = 4
    secretNo = generateNo(noLength)
    # print(secretNo)
    guessNo(secretNo)

if __name__ == '__main__':
    main()