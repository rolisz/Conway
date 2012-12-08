import copy

__author__ = 'Roland'


class Universe:
    def __init__(self):
        self.list = {}

    def AddCell(self,x,y):
        self.list[(x,y)] = 1

    def CellCount(self):
        return len(self.list)

    def GetCell(self,x,y):
        return (x,y) if (x,y) in self.list else None

    def NeighbourFor(self,cell1,cell2):
        return (abs(cell1[1]-cell2[1]) == 1 and cell1[0] == cell2[0])\
               or (abs(cell1[0] - cell2[0]) == 1 and cell1[1]==cell2[1])  \
               or abs(cell1[1] - cell2[1]) == abs(cell1[0] - cell2[0]) == 1

    def CountCellNeighbors(self,cell):
        return len([celula for celula in self.list if self.NeighbourFor(cell,celula)])

    def tick(self):
        newList = {}
        for cell in self.list:
            pass



