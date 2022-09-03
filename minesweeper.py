import random

#numbers for mine indicators, 9 resembles a mine
values = [str(i) for i in range(10)]


mine_frequency = 5

class grid:
    def __init__(self, height: int, width: int):
        self.list = [[0 for _ in range(width)] for _ in range(height)]
        self.height = height
        self.width = width

        self.generateNewGrid()

    def generateNewGrid(self):
        #generate mine indexes
        bombs = random.sample(range(self.height * self.width), self.height * self.width // 5)

        #place mine and update neighbours number if they're not a mine themselves
        for index in bombs:
            i = index // self.width
            j = index % self.width

            self.list[i][j] = 9

            for h in (-1, 0, 1):
                for w in (-1, 0, 1):
                    try:
                        if i+h >= 0 and j+w >= 0 and not isBomb(self.list[i + h][j + w]):
                            self.list[i + h][j + w] += 1
                    except:
                        pass



def isBomb(val: int):
    return val == 9


def printListOfLists(list_of_lists):
    for list in list_of_lists:
        print(list)


g = grid(5, 5)
printListOfLists(g.list)
