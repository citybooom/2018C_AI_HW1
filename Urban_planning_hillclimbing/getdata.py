"""get the data from file."""


def getdata(a):
    """Stop the docstring warining please."""
    with open(a, 'r') as f:
        dt = f.readlines()  # get data from txt file
    indu = int(dt[0])  # how many industrial sites
    comm = int(dt[1])  # how many commercial sites
    resi = int(dt[2])  # how many residential sites

    Nx = int(((len(dt[3])+1)/2))  # get the x size of the map
    Ny = len(dt) - 3  # get the y size of the map
    toxic = []
    scenic = []
    # get the map
    mymap = [[0 for x in range(Nx)] for y in range(Ny)]

    for i in range(3, len(dt)):
        for j in range(0, len(dt[3])-1):
            if dt[i][j] != ',':
                if dt[i][j] == 'X':
                    mymap[i-3][int((j+1)/2)] = 'X'
                    toxic.append([i-3, int((j+1)/2)])
                elif dt[i][j] == 'S':
                    mymap[i-3][int((j+1)/2)] = 'S'
                    scenic.append([i-3, int((j+1)/2)])
                else:
                    mymap[i-3][int((j+1)/2)] = int(dt[i][j])

    # print(mymap)
    # mmp = [[0 for x in range(5)] for y in range(5)]
    # print(type(mmp[1][1]))
    # mylist = [[1, 2], [1, 3]]
    # print(mylist[1][1])
    # yourlist = []
    # print(yourlist)

    return(indu, comm, resi, mymap, toxic, scenic, Nx, Ny)
