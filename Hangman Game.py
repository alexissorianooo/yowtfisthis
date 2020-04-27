#project 5

#import
import random, os

#globals
words=["cookie", "good", "coffee", "pizza"]
ctr=5
blankLines=[]
numLet=[]
ansletter=[]
blankLinesSave=[]

def randWord():
    num=random.randint(0,3)
    wordDef(num)

def wordDef(x):
    print("Definition:\n")
    if x==0:
        print("A small sweet cake, typically round, flat, and crisp.")
    if x==1:
        print("That which is morally right; righteousness.")
    if x==2:
        print("A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub.")
    if x==3:
        print("A dish of Italian origin consisting of a flat, round base of dough baked with a topping of tomato sauce and cheese, typically with added meat or vegetables.")
    userQues(x)

def wordDef1(x):
    global blankLines,blankLinesSave
    word = words[x]
    os.system('cls')
    blankLinesSave=blankLines
    print("Definition:\n")
    if x==0:
        print("A small sweet cake, typically round, flat, and crisp.")
    if x==1:
        print("That which is morally right; righteousness.")
    if x==2:
        print("A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub.")
    if x==3:
        print("A dish of Italian origin consisting of a flat, round base of dough baked with a topping of tomato sauce and cheese, typically with added meat or vegetables.")

    #show choices again
    print("\nLetter Choices:")
    ansletter=list(word.lower())
    for l in range(0,4):
        letter=randLetter()
        random.shuffle(ansletter)
        ansletter.append(letter)
    for a in ansletter:
        print(a, end=" ")

    print("\n\nRevealed Answer")
    print(" ".join(blankLines))

    blankLinestemp=list(blankLines)
    blankLinesSort=blankLinestemp
    blankLinesSort.sort()
    for i in range(len(blankLines)):
        while blankLinesSort[0] == "_":
            ans(x)
        print("\n\nCongratulations! You completed the minigame!")
        input("\n\nPress any key to continue..")
        exit()
    

def userQues(x):
    global blankLines,numLet
    word = words[x]
    lenght=int(len(word))#used for hint
    numLet=list(word)#used for blankLines.extend
    numLi=len(numLet)#used to chnage letters to underlines
    blankLines.extend(numLet)
    print("\nWhat is the word?")
    print("Hint: {0} letters\n".format(lenght))
    for i in range(numLi): #changing to underlines
        blankLines[i]="_"
    print(" ".join(blankLines)) #printing underlines

    #for choices original
    print("\nLetter Choices:")
    ansletter=list(word.lower())# used to list letters per word
    for l in range(0,4):
        letter=randLetter() #generates random letter for choices
        random.shuffle(ansletter) #shuffling the letters in the correct answer
        ansletter.append(letter) #adding random generated letters
    for a in ansletter:
        print(a, end=" ") #printing choices
    ans(x)
    
    #user guessing
def ans(x):
    global ctr, blankLines, ansletter
    word=words[x]
    #print("\n\nYour lives left {0}".format(ctr))
    guess=str(input("\n\nEnter any letter: "))
    guess=guess.lower()#lowercase user's answer
    for i in range (len(word)):#searching every letter 
        if numLet[i]==guess: #WHEN CORRECT
            blankLines[i]=guess#replacing underline to correct letter
            print(" ".join(blankLines)) #printing
    input("press any key to continue..")
    wordDef1(x)
        
    
    
def randLetter(): #random letter generator
    letters="qwertyuiopasdfghjklzxcvbnm"
    randLet = random.randint(0,25)
    letter = letters[randLet]
    return letter

usr=input("Generate word [Y/N]: ") #main
if usr=="y" or usr=="Y":
    randWord()

