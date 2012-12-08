__author__ = 'Roland'

import main

def DefineUniverse():
    universe= main.Universe()
    universe.AddCell(1,1)
    universe.AddCell(1,2)
    assert(universe.CellCount()==2)
    print("DefineUniverse green")

DefineUniverse()
def CellIsDefinedInUniverse():
    universe= main.Universe()
    universe.AddCell(1,1)

    cell1=universe.GetCell(1,1)
    assert(cell1 !=None)
    print("CellIsDefinedInUniverse green")

CellIsDefinedInUniverse()
def CellIsNotDefinedInUniverse():
    universe= main.Universe()

    cell1=universe.GetCell(2,1)
    assert(cell1 ==None)
    print("CellIsNotDefinedInUniverse green")

CellIsNotDefinedInUniverse()
def CellNeighbouringOnHorizontal():
    universe= main.Universe()
    universe.AddCell(1,1)
    universe.AddCell(1,2)

    cell1=universe.GetCell(1,1)
    cell2=universe.GetCell(1,2)
    assert(universe.NeighbourFor(cell1,cell2))
    print("CellNeighbouringOnHorizontal green")
def CellNeighbouringOnHorizontalPre():
    universe= main.Universe()
    universe.AddCell(1,1)
    universe.AddCell(1,0)

    cell1=universe.GetCell(1,1)
    cell2=universe.GetCell(1,0)
    assert(universe.NeighbourFor(cell1,cell2))
    print("CellNeighbouringOnHorizontal green")

def NotCellNeighbouringOnHorizontal():
    universe= main.Universe()
    universe.AddCell(1,1)
    universe.AddCell(1,3)

    cell1=universe.GetCell(1,1)
    cell2=universe.GetCell(1,3)
    assert(not universe.NeighbourFor(cell1,cell2))
    print("NotCellNeighbouringOnHorizontal green")

CellNeighbouringOnHorizontal()
CellNeighbouringOnHorizontalPre()
NotCellNeighbouringOnHorizontal()

def CellNeighbouringOnVertical():
    universe= main.Universe()
    universe.AddCell(0,1)
    universe.AddCell(1,1)

    cell1=universe.GetCell(1,1)
    cell2=universe.GetCell(0,1)
    assert(universe.NeighbourFor(cell1,cell2))
    print("CellNeighbouringOnVertical green")
def CellNeighbouringOnVerticalPre():
    universe= main.Universe()
    universe.AddCell(2,1)
    universe.AddCell(1,1)

    cell1=universe.GetCell(1,1)
    cell2=universe.GetCell(2,1)
    assert(universe.NeighbourFor(cell1,cell2))
    print("CellNeighbouringOnVertical green")

def NotCellNeighbouringOnVertical():
    universe= main.Universe()
    universe.AddCell(0,1)
    universe.AddCell(2,1)

    cell1=universe.GetCell(0,1)
    cell2=universe.GetCell(2,1)
    assert(not universe.NeighbourFor(cell1,cell2))
    print("NotCellNeighbouringOnHorizontal green")


CellNeighbouringOnVertical()
CellNeighbouringOnVerticalPre()
NotCellNeighbouringOnVertical()

def CellNeighbouringOnDiagonal():
    universe= main.Universe()
    universe.AddCell(0,0)
    universe.AddCell(1,1)

    cell1=universe.GetCell(1,1)
    cell2=universe.GetCell(0,0)
    assert(universe.NeighbourFor(cell1,cell2))
    print("CellNeighbouringOnDiagonal green")

def NotCellNeighbouringOnDiagonal():
    universe= main.Universe()
    universe.AddCell(0,0)
    universe.AddCell(2,1)

    cell1=universe.GetCell(0,0)
    cell2=universe.GetCell(2,1)
    assert(not universe.NeighbourFor(cell1,cell2))
    print("NotCellNeighbouringOnDiagonal green")

NotCellNeighbouringOnDiagonal()
CellNeighbouringOnDiagonal()

def CellNeighbouringOnReverseDiagonal():
    universe= main.Universe()
    universe.AddCell(0,1)
    universe.AddCell(1,0)

    cell1=universe.GetCell(0,1)
    cell2=universe.GetCell(1,0)
    assert(universe.NeighbourFor(cell1,cell2))
    print("CellNeighbouringOnReverseDiagonal green")

def NotCellNeighbouringOnReverseDiagonal():
    universe= main.Universe()
    universe.AddCell(0,2)
    universe.AddCell(2,1)

    cell1=universe.GetCell(0,2)
    cell2=universe.GetCell(2,1)
    assert(not universe.NeighbourFor(cell1,cell2))
    print("NotCellNeighbouringOnReverseDiagonal green")

CellNeighbouringOnReverseDiagonal()
NotCellNeighbouringOnReverseDiagonal()

def NotCellNeighbouringOnFarDiagonal():
    universe= main.Universe()
    universe.AddCell(0,0)
    universe.AddCell(2,2)

    cell1=universe.GetCell(0,0)
    cell2=universe.GetCell(2,2)
    assert(not universe.NeighbourFor(cell1,cell2))
    print("NotCellNeighbouringOnFarDiagonal green")

NotCellNeighbouringOnFarDiagonal()

def NumberofNeighbors():
    universe= main.Universe()
    universe.AddCell(0,0)
    universe.AddCell(0,1)

    cell1 = universe.GetCell(0,0)
    assert(universe.CountCellNeighbors(cell1) == 1)

def LonelyCellDies():
    universe= main.Universe()
    universe.AddCell(0,0)
    universe.AddCell(0,1)
    universe.tick()

    assert(universe.CellCount() == 0)
    print("LonelyCellDies green")

LonelyCellDies()