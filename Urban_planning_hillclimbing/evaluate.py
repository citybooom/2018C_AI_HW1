"""this module calculates the points we get."""
import copy


def evaluate(mymap1, positions, toxic, scenic, indu, comm, resi, Nx, Ny):
    """Get evaluation for the map."""
    # get the realmap & get building cost
    realmap = copy.deepcopy(mymap1)
    cost_building = 0
    for i in range(0, len(positions)):
        if i <= indu+comm+resi:
            if isinstance(mymap1[positions[i][0]][positions[i][1]], int):
                cost_building = cost_building - \
                    mymap1[positions[i][0]][positions[i][1]]

        if i >= 0 and i < indu:
            realmap[positions[i][0]][positions[i][1]] = 'I'
        if i >= indu and i < indu+comm:
            realmap[positions[i][0]][positions[i][1]] = 'C'
        if i >= indu+comm and i < indu+comm+resi:
            realmap[positions[i][0]][positions[i][1]] = 'R'

    # print(realmap)
    # print(cost_building)

    """evaluate industrial, commercial, and residential."""
    induvalue = 0
    commvalue = 0
    resivalue = 0
    for i in range(0, len(positions)):
        # industrial value
        if i >= 0 and i < indu:
            for pos in [[x, y] for x in range(0, Ny) for y in range(0, Nx)
                        if abs(x-positions[i][0]) +
                        abs(y-positions[i][1]) <= 2 and abs(x-positions[i][0])
                        + abs(y-positions[i][1]) != 0]:
                # print('inn', realmap[pos[0]][pos[1]])
                if realmap[pos[0]][pos[1]] == 'I':
                    induvalue = induvalue + 3
                    # print('in')
                if realmap[pos[0]][pos[1]] == 'X':
                    # print('in-')
                    induvalue = induvalue - 10

        # commercial value
        if i >= indu and i < indu+comm:
            for pos in [[x, y] for x in range(0, Ny) for y in range(0, Nx)
                        if abs(x-positions[i][0]) +
                        abs(y-positions[i][1]) <= 2 and abs(x-positions[i][0])
                        + abs(y-positions[i][1]) != 0]:
                if realmap[pos[0]][pos[1]] == 'C':
                    commvalue = commvalue - 5
                if realmap[pos[0]][pos[1]] == 'X':
                    commvalue = commvalue - 20
                if realmap[pos[0]][pos[1]] == 'R':
                    commvalue = commvalue + 5
            for pos in [[x, y] for x in range(0, Ny) for y in range(0, Nx)
                        if abs(x-positions[i][0]) +
                        abs(y-positions[i][1]) == 3]:
                if realmap[pos[0]][pos[1]] == 'R':
                    commvalue = commvalue + 5

        # residential value
        if i >= indu+comm and i < indu+comm+resi:
            for pos in [[x, y] for x in range(0, Ny) for y in range(0, Nx)
                        if abs(x-positions[i][0]) +
                        abs(y-positions[i][1]) <= 2 and abs(x-positions[i][0])
                        + abs(y-positions[i][1]) != 0]:
                if realmap[pos[0]][pos[1]] == 'X':
                    resivalue = resivalue - 20
                if realmap[pos[0]][pos[1]] == 'I':
                    resivalue = resivalue - 5
                if realmap[pos[0]][pos[1]] == 'C':
                    resivalue = resivalue + 5
                if realmap[pos[0]][pos[1]] == 'S':
                    resivalue = resivalue + 10
            for pos in [[x, y] for x in range(0, Ny) for y in range(0, Nx)
                        if abs(x-positions[i][0]) +
                        abs(y-positions[i][1]) == 3]:
                if realmap[pos[0]][pos[1]] == 'I':
                    resivalue = resivalue - 5
                if realmap[pos[0]][pos[1]] == 'C':
                    resivalue = resivalue + 5

    totalcost = cost_building + induvalue+commvalue+resivalue

    return(totalcost, realmap)
    # print(induvalue)
    # print(commvalue)
    # print(resivalue)
    # print(totalcost)
