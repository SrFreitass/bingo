from random import randint

class Generate_cols():
    def __init__(self, letters, matrix) -> None:
        self.letters: dict = letters
        self.matrix: list[list[int]] = matrix


    def execute(self, letter):
        min, max = self.letters.get(letter)
        for i in range(len(self.matrix)):
            col = list(self.letters.keys()).index(letter)

            if(col == 2 and i == 2):
                self.matrix[col].append("*")
            else:
                number = randint(min, max)

                while number in self.matrix[col]:
                    number = randint(min, max)

                self.matrix[col].append(number)
                
    