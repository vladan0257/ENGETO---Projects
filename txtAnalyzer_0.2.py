"""
txtAnalyzer_0.2.py: první projekt do Engeto Online Python Akademie
author: Vladan Pivovarnik
email: v.pivovarnik@seznam.cz
discord username: vladan0257
"""
from tabulate import tabulate

def login(name, password):
    """
    Returns True if user name and password are found in a predefined local dictionary.
    Param. name: User typed-in name as str.
    Param. passwrod: User typed-in password as str.
    """  
    registeredUsers = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
    dictPassword = registeredUsers.get(name)
    return True if password == dictPassword else False

# Defining printable dashed line
dashLine = 40 * '-'

# Storing user' inputs.
inputName = input('Type your username and press enter: ')
inputPassword = input('Type your password and press enter: ')
print(dashLine)

loggedIn = login(inputName, inputPassword)

# Evaluation of user credentials. If matches with one of predefined name-password pairs, an external file is loaded and user is informed on how to choose
# one of available texts. If the file is not available or if user credentials will not match one of stored name-password pairs, the program will close.
if loggedIn:
    print(f'Login success, {inputName}!')
    try:
        from task_template import TEXTS
        print('You\'ve got 3 texts to be analyzed.', dashLine, sep='\n')
    except:
        print('However I\'am unable to load texts for analysis.')
        exit()
else:
    print('You\'re not a registered user. Terminating the program...')
    exit()

# A prompt for user chosen text
txtNo = input('Press 1, 2 or 3 choosing one of them: ')

# Processing the analysis, storing and printing results if correct user input.
if txtNo.isdigit() and int(txtNo) in range(1, 4, 1):
    print('Processing the analysis...', dashLine, sep='\n')

    txt = TEXTS[int(txtNo) - 1]

    words = sum(element.strip(',.').isalpha() for element in txt.split())
    print(f'There are {words} words.')

    title = sum(element.istitle() for element in txt.split())
    print(f'There are {title} titlecase words.')

    upper = sum(element.isupper() for element in txt.split())
    print(f'There are {upper} uppercase words.')

    lower = sum(element.islower() for element in txt.split())
    print(f'There are {lower} lowercase words.')

    num = sum(element.isnumeric() for element in txt.split())
    print(f'There are {num} numeric words.')

    sumNum = sum(float(element) for element in txt.split() if element.isdigit())
    print(f'The sum of all the numbers is {int(sumNum) if sumNum.is_integer() else sumNum}.')

    # This chunk of code is (1st line): slicing the text into single words. Then we get the number of characters in each word from beginning 
    # to the end of the text using len() function and storing those numbers into a single list meaning 1 number = length of the 1 word.
    # (2nd line): We then go through each single number and count, how many times it occurs in the list, which gives us base for creating 
    # a dictionary with length of the word as the key and number of its occurences as the value. In the time we initiate key-value pairs 
    # a 2nd value is also being assigned to each key so we can get nice visual representation of the word-length-distribution.
    # (3rd line): 3rd line of the code is simply sorting lengths of the words from minimum to maximum.
    wordsLengthTab = [len(element) for element in txt.split() if element.strip(',.').isalpha()]
    wordsLengthDict = {wordsLength: (wordsLengthTab.count(wordsLength) * '*', wordsLengthTab.count(wordsLength)) for wordsLength in wordsLengthTab}
    wordsLengthDict = dict(sorted(wordsLengthDict.items()))
    print(dashLine)
    print(tabulate([(key,) + val for key, val in wordsLengthDict.items()], headers=['LEN', 'OCCURENCES', 'NO'], tablefmt='psql', numalign='left'))

elif txtNo.isdigit() and int(txtNo) not in range(1, 4, 1):
    print('You\'ve chosen some out-of-range-number. Terminating the program...')
    exit()

else:
    print('Your input might not even be a number. Terminating the program...')
    exit()

input('Press any key to exit.')