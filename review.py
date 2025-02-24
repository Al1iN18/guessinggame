from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guessing Game")
        #self.inputNumber = self.addLabel(text="Guess a number 1 to 100" )
        self.try_count = 0
        

        greeting = "Guess a number 1 to 100"
        self.hint = self.addLabel(text= greeting, row= 0, column=0, sticky = "NSEW")


        self.guessComp = random.randint(1, 100)
        self.addLabel("Your guess:", row=1, column=0)
        self.guess_field= self.addIntegerField(0, row=1,column=1)
        
        self.next_btn = self.addButton(text="Next Guess", row=3, column=0, command= self.nextGuess)
        self.new_game = self.addButton(text="New Game", row=3, column=3, command=self.newGame)
        

    def nextGuess(self):
        self.try_count += 1
        guess = self.guess_field.getNumber()
        if guess == self.guessComp:
            self.hint["text"]= f'You have guessed the number ${self.try_counts} attempts!'
            self.next_btn["state"]= "disabled"
        elif guess < self.guessComp:
            self.hint["text"] = "Sorry your # too small!"
        else:
            self.hint["text"] = "Sorry your # is to Big!"


    def newGame(self):
        #reset GUI to oringal state
        self.guessComp = random.randint(1, 100)
        self.try_count = 0
        greeting = "Guess a number 1 to 100"
        self.hint ["text"] = greeting
        self.guess_field.setNumber(0)
        self.next_btn["state"] = "normal"
        #def checkanswer()
        #    if guess == keynumber print ("You have won!")
        #    elif guess > keynumber print "guess again! your guess is to high"
        #    elif guess < keynumber print "guess again! your guess is to low"

        #2nd label with input button
        #function that takes guess match it with random and print a or b
        # make select a random number and save into keynumber
        #   
        # count each loop and save into a final guessing count

def main():
    GuessingGame().mainloop()
if __name__=="__main__":
    main()


        #button next guess
        #button new game
