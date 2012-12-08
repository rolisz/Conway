__author__ = 'Roland'

import main

def test_matrice():
    m = main.matrice()
    assert(m.get(0,0) == 0)

    m.set(0,0)
    assert(m.get(0,0) == 1)

    m.die(0,0)
    assert(m.get(0,0) == 0)
    m.die(0,0)
    print("all clear")

    m.set(1,1)
    m.set(1,2)
    print(m.nrNeighbors(2,1))
    assert(m.nrNeighbors(2,1) == 2)

    assert(m.nrNeighbors(1,1) == 1)

    assert(len(m.deadNeighbors(1,1)) == 7)

test_matrice()

def test_universe():
    m = main.matrice()
    m.set(0,0)
    m = main.tick(m)
    assert(m.get(0,0) == 0)

    m.set(0,0)
    m.set(0,1)
    m.set(1,1)
    m.set(1,0)

    m = main.tick(m)

    assert(m.get(1,0) == 1)
    assert(m.get(0,0) == 1)
    assert(m.get(1,1) == 1)
    assert(m.get(0,1) == 1)

    m = main.matrice()
    m.set(0,0)
    m.set(-1,0)
    m.set(1,0)
    m = main.tick(m)
    assert(m.get(0,0) == 1)
    assert(m.get(-1,0) == 0)
    assert(m.get(1,0) == 0)
    assert(m.get(0,1) == 1)
    assert(m.get(0,-1) == 1)
    assert(m.get(1,1) == 0)

test_universe()

import tkinter

master = tkinter.Tk()

w = tkinter.Canvas(master, width=400, height=400)
w.pack()
m = main.matrice()
m.set(0,0)
m.set(-1,0)
m.set(1,0)
m.set(5,3)
m.set(10,4)
for cell in m.list:
    w.create_rectangle(cell[0]*10, cell[1]*10, cell[0]*10+10, cell[1]*10+10, fill="blue")

m = main.tick(m)
assert(m.get(0,0) == 1)
assert(m.get(-1,0) == 0)
assert(m.get(1,0) == 0)
assert(m.get(0,1) == 1)
assert(m.get(0,-1) == 1)
assert(m.get(1,1) == 0)


tkinter.mainloop()