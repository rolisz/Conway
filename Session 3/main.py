import copy

class matrice:

    def __init__(self):
        self.list = {}

    def get(self,x,y):
        return 1 if (x,y) in self.list else 0

    def set(self,x,y):
        self.list[(x,y)] = 1

    def die(self,x,y):
        if (x,y) in self.list:
            del self.list[(x,y)]

    def nrNeighbors(self,x,y):
        count = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if (i!= x or j!=y) and self.get(i,j):
                    count+= 1
        return count

    def deadNeighbors(self,x,y):
        return [(i,j) for i in range(x-1,x+2) for j in range(y-1,y+2) if (i,j) != (x,y) and not self.get(i,j)]

def tick(univers):
    neighbors = set()
    newUnivers = copy.deepcopy(univers)
    for cells in univers.list:
        nrNeigbors = univers.nrNeighbors(cells[0],cells[1])
        if nrNeigbors < 2 or nrNeigbors > 3:
            newUnivers.die(cells[0],cells[1])
        neighbors = neighbors.union(set(univers.deadNeighbors(cells[0],cells[1])))
    for cells in neighbors:
        if univers.nrNeighbors(cells[0],cells[1]) == 3:
            newUnivers.set(cells[0],cells[1])
    return newUnivers


