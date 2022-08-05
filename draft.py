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
    
    grays = set()
    yellows = [set() for i in range(5)]
    greens = [' '] * 5
    answerSet = set()

    def __init__(self):
        fhand = open('wordleanswers.txt')
        for line in fhand:
            self.answerSet.add(line.rstrip())
        fhand.close()
    
    def play_guess(self, rawinput, checker):
        input = str(rawinput)
        feedback = checker.validate(input)
        print(''.join([str(i) for i in feedback]))
        initial = len(self.answerSet)
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
        print(initial - len(self.answerSet))
        print(self.answerSet)
        print()
            
class game:
    solution = ""
    checker = None
    player = None
    turnCounter = 0

    def __init__(self, solution):
        self.checker = guesschecker(solution)
        self.player = wordlebot()
    
    def user_play(self):
        while(self.turnCounter < 6):
            self.turnCounter += 1
            x = input("guess a 5-letter word: ")
            if self.checker.correct(x):
                print("you win! you guessed the word in", self.turnCounter, "attempt(s)")
                return
            self.player.play_guess(x, self.checker)

        print("you lose! better luck next time. the solution to this one was", self.solution)
    
    def auto_play(self, starter = "alert"):
        while(self.turnCounter < 6):
            self.turnCounter += 1
            x = starter if self.turnCounter == 1 else list(self.player.answerSet)[0]
            print("bot is now guessing", x)
            if self.checker.correct(x):
                print("bot wins! it guessed the word in", self.turnCounter, "attempt(s)")
                return self.turnCounter
            self.player.play_guess(x, self.checker)
        print("bot loses! better luck next time. the solution to this one was", self.solution)


g = game("buggy")
g.auto_play() 