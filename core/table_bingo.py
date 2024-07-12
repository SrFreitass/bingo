from random import randint

class Table_Bingo:
    def __init__(self, letters: dict[str, list[int]]) -> None:
        self.letters = letters

    def execute(self) -> list[list[int]]:
        print("LOG: Gerando nova tabela de bingo!")
        matrix = []
        for x in range(5):
            matrix.append([])

        for letter in self.letters.keys():
            min, max = self.letters.get(letter)
            for i in range(len(matrix)):
                col = list(self.letters.keys()).index(letter)

                if(i == 2 and letter == "N"):
                    matrix[col].append("*")
                else:
                    number = randint(min, max)
                    while number in matrix[col]:
                        number = randint(min, max)

                    matrix[col].append(number)
        return matrix