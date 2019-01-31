##Project 2: Make a snowman game, for this example the snowman has 5 limbs

def main():
    instructions()
    import random
    f = open('smwords.py','r')
    words = f.readlines()
    f.close()
    i = 0
    for word in words:
        word= word.strip()
        words[i] = word
        i +=1
    secretWord = random.choice(words) ## have to strip the /n/ space at the end
    rightGuess = ['_']*len(secretWord)
    wrongGuess = []
    snowMan = [[' ',' ',' '],
               [' ',' ',' '],
               [' ',' ',' '],
               [' ',' ',' ']]
    wrongCount = 0
    rG=''
    player1name = input('Player 1 enter your name: ')
    player2name = input('Player 2 enter your name: ')
    turn = 0
    
    while rG != secretWord and wrongCount <8:
        if turn%2 == 0:
            player = player1name
        else:
            player = player2name
        rG=''
        guess = 'a'
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        guess = getGuess(player,wrongGuess)
        if guess in alphabet:
            if guess not in wrongGuess:                   
                if guess in secretWord:
                    print('Correct!')
                    i = 0
                    for i in range (0, len(secretWord)):
                        if guess == secretWord[i]:
                            rightGuess[i] = guess
                else:
                    print('Incorrect!')
                    wrongCount+=1
                    wrongGuess.append(guess)
                    snowMan = buildSM(wrongCount,snowMan)
                
                for items in rightGuess:
                    rG = str(rG + ("".join(str(items))))
                
                    
                print('Right guesses so far...')
                print(*rightGuess)
                print(' ')
                print('Wrong guesses so far...')
                print(*wrongGuess)
                print(' ')
                print('Snowman progress... ')
                printPretty(snowMan)
                print(' ')
                turn +=1
            else: print('You have already guessed that wrong letter. Guess again. ')
        else:
            print('Only enter lowercase characters of the alphabet. Try again')
    
    report(rG, secretWord, player)


def instructions():
    print('To play snowman, you will have to take turns guessing letters until you can correctly identify the word. However, each time you guess incorrectly, a part of a snowman will be added. If the full snowman is built before you guess the secret word, you lose the game!')

def getGuess(p,wg):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    g = 'a'
    while g in alphabet:
        g = str.lower(input('Guess a letter ' + p + ' '))
        if g not in wg:
            return(g)
        else:
            print('You have already guessed that wrong letter. Try again!')
    print('Only enter lowercase charcters of the alphabet. Try again.')
    
def report(j,k,p):
    if j == k: # must convert my list of rightGuess to a string for final comparison
        print('Congratulations ' + p + ' you have correctly guessed the word ' + j + ' before the snowman was complete.')
    else:
        print('You have built a full snowman and run out of chances to guess! Game over!')

def buildSM (w,s):
    if w == 1:
        s[3][0] = ('~')
    elif w == 2:
        s[3][1] = ('~')
    elif w == 3:
        s[3][2] = ('~')
    elif w == 4:
        s[0][1] = ('O')
    elif w == 5:
        s[1][1] = ('O')
    elif w == 6:
        s[2][1] = ('O')
    elif w == 7:
        s[1][2] = ('\\')
    elif w == 8:
        s[1][0] = ('/')
    return(s)

def printPretty(g):
    numOfrows = len(g)
    rowLength = len(g[0])
    for r in range(numOfrows):
        for c in range (rowLength):
            print(" " + str(g[r][c]),end="")
        print( )                                                      

##just have to figure out the capitalization, user friendly-ness

