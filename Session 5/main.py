import copy

def cell_lives_in_next_generation(previous_state, neighbour_count):
    if previous_state and (neighbour_count < 2 or neighbour_count > 3):
        return False
    if not previous_state and neighbour_count == 3:
        return True
    return previous_state

class Universe():
    def __init__(self):
        self._cells = set()

    def cellCount(self):
        return len(self._cells)

    def resurect(self, line, column):
        self._cells.add((line, column))

    def die(self, line, column):
        self._cells = self._cells - {(line, column)}

    def nrNeighbors(self, line, column):
        deltas = ((-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1))
        return len([True for dx, dy in deltas if (line + dx, column + dy) in self._cells])

    def deadNeighbors(self,line,column):
        deltas = ((-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1))
        return {(line + dx, column + dy) for dx, dy in deltas if (line + dx, column + dy) not in self._cells}

    def __eq__(self, other):
        return self._cells == other._cells


    def tick(self):
        deadNeighbors = set()
        newUniverse = copy.deepcopy(self)
        for cell in self._cells:
            if not cell_lives_in_next_generation(True,self.nrNeighbors(*cell)):
                newUniverse.die(*cell)
            deadNeighbors =  deadNeighbors.union(self.deadNeighbors(*cell))
        for deadCell in deadNeighbors:
            if cell_lives_in_next_generation(True,self.nrNeighbors(*deadCell)):
                newUniverse.resurect(*cell)
        return newUniverse





