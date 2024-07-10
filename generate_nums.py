from random import randint

class Generate_num():  
    def __init__(self, drawn: list, min_n: int, max_n: int) -> None:
        self.min_n = min_n
        self.max_n = max_n
        self.drawn = drawn
        pass

    def execute(self):
        number = randint(self.min_n, self.max_n)
        while number in self.drawn:
            number = randint(self.min_n, self.max_n)
        self.drawn.append(number)
        print(number)
        return number

        