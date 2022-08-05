'''
gray:               letter is not anywhere in the answer
order:              does not matter at all 
data structure:     set()

yellow:             letter is in the word but not at that index
order:              order is important - index dependent, can hold multiple values 
data structure:     5-wide list of set()

green:              letter is in solution at that exact index
order:              very important - index dependent, only one value
data structure:     5-wide list
'''

from logging import FileHandler
from statistics import mean
import string

class guesschecker:

    
    def __init__(self, answer):
        self.answer = answer
    
    def validate(self, guess):
        retval = [0] * 5
        for i in range(5):
            if self.answer[i] == guess[i]:
                retval[i] = 2
            elif guess[i] in self.answer:
                retval[i] = 1
        return retval
    
    def correct(self, guess):
        if guess == self.answer:
            return True
        return False

class wordlebot:
    
    grays = None
    yellows = None
    greens = None
    answerSet = set()
    frequencies = dict(zip(list(string.ascii_lowercase), [0] * 26))

    def __init__(self):
        fhand = open('wordleanswers.txt')
        for line in fhand:
            self.answerSet.add(line.rstrip())
            for i in line.rstrip():
                self.frequencies[i] += 1
        fhand.close()
        self.grays = set()
        self.yellows = [set() for i in range(5)]
        self.greens = [' '] * 5

    def play_guess(self, rawinput, checker):
        #print("LENGTH OF ANSWER SET IS: ", len(self.answerSet))
        input = str(rawinput)
        feedback = checker.validate(input)
        #print(''.join([str(i) for i in feedback]))
        #initial = len(self.answerSet)
        for i in range(5):
            if feedback[i] == 0:
                self.grays.add(input[i])
                for word in self.answerSet.copy():
                    if input[i] in word:
                        self.answerSet.remove(word)
            elif feedback[i] == 1:
                self.yellows[i].add(input[i])
                for word in self.answerSet.copy():
                    for char in self.yellows[i]:
                        if word[i] == char or char not in word:
                            self.answerSet.remove(word)
                            break
            else:
                self.greens[i] = input[i]
                for word in self.answerSet.copy():
                    if word[i] != self.greens[i]:
                        self.answerSet.remove(word)
        #print(len(self.answerSet)) 
        #print(self.answerSet)            
class game:
    solution = ""
    checker = None
    player = None
    turnCounter = 0
    

    def __init__(self, solution):
        self.checker = guesschecker(solution)
        self.player = wordlebot()
        self.turnCounter = 0
        
    def user_play(self):
        while(self.turnCounter < 6):
            self.turnCounter += 1
            x = input("guess a 5-letter word: ")
            if self.checker.correct(x):
                print("you win! you guessed the word in", self.turnCounter, "attempt(s)")
                print()
                return self.turnCounter
            self.player.play_guess(x, self.checker)

        print("you lose! better luck next time. the solution to this one was", self.solution)
        print()
        return -1
    
    def auto_play(self, x = "alert"):
        while(self.turnCounter < 6):
            self.turnCounter += 1
            #print("bot is now guessing", x)
            if self.checker.correct(x):
                #print("bot wins! it guessed the word in", self.turnCounter, "attempt(s)")
                #print()
                return self.turnCounter
            self.player.play_guess(x, self.checker)
            msf = sum([self.player.frequencies[i] for i in list(self.player.answerSet)[0]])
            x = list(self.player.answerSet)[0]
            for word in self.player.answerSet:
                if sum([self.player.frequencies[i] for i in word]) > msf:
                    msf = sum([self.player.frequencies[i] for i in word])
                    x = word

        #print("bot loses! better luck next time. the solution to this one was", self.solution)
        #print()
        return -1


def test_play(solution):
    g = game(solution)
    return g.user_play()

def test_autoplay(solution):
    g = game(solution)
    return g.auto_play()

def statFinder():
    suc = 0
    fail = 0
    totalguess = 0
    fhand = open('wordleanswers.txt')
    for line in fhand:
        x = test_autoplay(line.rstrip())
        if x > 0:
            suc +=1
            totalguess += x
        else:
            print(line.rstrip())
            fail += 1
    
    print("number of successes:", suc)
    print("average number of guesses:", totalguess/suc)
    print("number of failures:", fail)
    print("success rate", suc/(suc+fail))
    print()

statFinder()
#test_play("yearn")
#test_autoplay("baker")