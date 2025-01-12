import random

class PasswordGenerator():
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numbers = '0123456789'
        self.symbols = '!#$%&()*+'
        self.choices = [self.letters, self.numbers, self.symbols]
        self.nr_letters = random.randint(8, 10)
        self.nr_symbols = random.randint(2, 4)
        self.nr_numbers = random.randint(2, 4)
        self.pass_length = self.nr_letters + self.nr_symbols + self.nr_numbers
        self.password = ""

    def generate(self):
        while self.pass_length > 0:
            rand_choice = random.choice(self.choices)
            if rand_choice == self.letters and self.nr_letters > 0:
                self.password = self.password + random.choice(self.letters)
                self.nr_letters -= 1
                self.pass_length -= 1
            if rand_choice == self.numbers and self.nr_numbers > 0:
                self.password = self.password + random.choice(self.numbers)
                self.nr_numbers -= 1
                self.pass_length -= 1
            if rand_choice == self.symbols and self.nr_symbols > 0:
                self.password = self.password + random.choice(self.symbols)
                self.nr_symbols -= 1
                self.pass_length -= 1

        return ''.join(random.sample(self.password, len(self.password)))