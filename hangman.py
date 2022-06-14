from invalidassignmentexception import InvalidAssignmentException

class Hangman():
    def __init__(self):
        self.word = ''
        self.lifes = 5
        self.prefix = 'Lifes: ' + str(self.lifes) + ' - Word: '
        self.guess = '_ _ _ _ _ _ _ _ '
        self.display = self.prefix + self.guess
    
    def set_word(self, word):
        self.word = word.lower()
        self.guess = '_ ' * len(self.word)
        self.display = self.prefix + self.guess
    
    def assign(self, letter):
        letter = letter.lower()
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guess = self.guess[:2 * i] + (letter + ' ') + self.guess[2 * i + 2:]
            self.display = self.prefix + self.guess
        else:
            self.lifes -= 1
            self.prefix = 'Lifes: ' + str(self.lifes) + ' - Word: '
            self.display = self.prefix + self.guess
    
    def show(self):
        return self.display

    def play(self):
        while self.lifes > 0:
            letter = input('Letter: ')
            self.assign(letter)
            print(self.display)
            if self.winner():
                return 'Ganaste'
        
        return 'Perdiste'
         
    
    def winner(self):
        return (self.guess).lower() == (' '.join(self.word) + ' ').lower()
    