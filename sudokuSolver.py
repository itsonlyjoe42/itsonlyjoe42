sudoku = [1, 0, 0, 9, 0, 0, 0, 0, 0,
          6, 7, 3, 0, 8, 5, 0, 9, 0,
          0, 0, 8, 0, 7, 0, 6, 1, 5,
          0, 0, 0, 7, 5, 0, 0, 6, 0,
          5, 0, 7, 4, 9, 0, 3, 2, 8,
          9, 0, 0, 0, 0, 0, 4, 0, 0,
          0, 0, 2, 0, 0, 1, 0, 4, 9,
          0, 8, 0, 0, 0, 0, 0, 7, 0,
          4, 0, 0, 0, 0, 0, 0, 0, 0]

# how many iterations

maxIters = 100

# how many runs

runs = 1000

import datetime

# print sudoku nicely

def nprint(sudoku):
    for id, i in enumerate(sudoku):
        if id % 9 == 0:
            print()
        elif id%3 == 0:
            print("|", end = " ")
        if id % 27 == 0:
            print("---------------------")
        if len(i) == 1:
            print(i[0], end = " ")
        else:
            print(i, end = " ")
    print("\n---------------------")

# remove from row/col/box

def rowColBoxOp(solve, rowindex, colindex, boxindex):
    test = 1
    for id, i in enumerate(solve):
        if len(i) == 1:
            val = i[0]
            [solve[k].remove(val) for k in rowindex[(id//9)] if val in solve[k] and len(solve[k]) > 1]
            [solve[k].remove(val) for k in colindex[id % 9] if val in solve[k] and len(solve[k]) > 1]
            [solve[k].remove(val) for k in boxindex[3 * (id // 27) + (id % 9) // 3] if val in solve[k] and len(solve[k]) > 1]
        else:
            test = 0
    return test

# Check rows/columns/boxes list for unique values

def unique(solve, rowColBoxIndex):

    for rowColBox in rowColBoxIndex:
        for num in range(1,10):
            count = 0
            for index in rowColBox:
                if count >= 2:
                    break
                elif num in solve[index]:
                    if len(solve[index]) == 1:
                        count = 2
                    else:
                        k = index
                        count +=1
                        l = num
            if count == 1:
                solve[k] = [l]

# Run all operations

def ops(solve, rowindex, colindex, boxindex, maxIters):

    i = 0
    while i < maxIters:
        test = rowColBoxOp(solve, rowindex, colindex, boxindex)
        if test:
            break

        unique(solve, rowindex)
        unique(solve, colindex)
        unique(solve, boxindex)

        i+=1

# For timimg

start = datetime.datetime.today()

# Specify box indices (can use this for irregular sudokus?)

boxindex = [[0, 1, 2, 9, 10, 11, 18, 19, 20]]
for j in range(1, 9):
    boxindex.append([i + j * 3 + int(j / 3) * 18 for i in boxindex[0]])

# Specify row locations

rowindex = [list(range(i, i+9)) for i in range(0, 80, 9)]
colindex = [list(range(i, 81, 9)) for i in range(0, 9)]

for run in range(runs):

    # create sudoku of possibilities

    solve = [[sudoku[i]] if sudoku[i] else list(range(1, 10)) for i in range(81)]

    # Solve

    ops(solve, rowindex, colindex, boxindex, maxIters)

end = datetime.datetime.today()

nprint(solve)

print(end - start)
