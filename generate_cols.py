from random import randint

class Generate_cols():
    def __init__(self, letters, min_n, max_n, matrix) -> None:
        self.min_n: int = min_n
        self.max_n: int = max_n
        self.letters: dict = letters
        self.matrix: list[list[int]] = matrix


    def execute(self, letter):
        min, max = self.letters.get(letter)
        for i in range(5):
            col = list(self.letters.keys()).index(letter)
            number = randint(min, max)

            while number in self.matrix[col]:
                number = randint(min, max)

            self.matrix[col].append(number)
            
    