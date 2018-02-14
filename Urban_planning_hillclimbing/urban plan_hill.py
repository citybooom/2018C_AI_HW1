"""this is the hill climbing version of urban planning."""
import time
import random
import getdata as getdata
import evaluate as evaluate
import copy

start_time = time.time()  # start_time
samplefile = 'sample 2.txt'
# get map and necessary data
# indu, comm, resi, mymap, toxic, scenic, Nx, Ny= \
# getdata.getdata('sample 2.txt')

deadline = 0.25
score = float('-inf')
oldscore = float('-inf')
newtime = float('inf')
# setup
iteration = 0
iteration1 = 0
while(time.time() - start_time <= deadline):
    # restart
    indu, comm, resi, mymap, toxic, scenic, Nx, Ny\
        = getdata.getdata(samplefile)
    randomseed = [[x, y] for x in range(0, Ny) for y in range(0, Nx)]
    for removeseed in toxic:
        if removeseed in randomseed:
            randomseed.remove(removeseed)

    positions = random.sample(randomseed, indu+comm+resi)  # original pos

    newscore, realmap = evaluate.evaluate(mymap, positions, toxic, scenic,
                                          indu, comm, resi, Nx, Ny)

    if newscore > score:
        score = newscore
        finalmap = copy.deepcopy(realmap)
        finaltime = time.time() - start_time

    oldscore = float('-inf')
    # get alterpos
    spacerem = copy.deepcopy(randomseed)
    for removepos in positions:
        spacerem.remove(removepos)

    # new round start
    realposition = copy.deepcopy(positions)
    iteration = iteration+1
    while(newscore > oldscore):
        # get the best score
        iteration1 = iteration1 + 1
        oldscore = newscore
        temp_score = float('-inf')
        new_positions = copy.deepcopy(realposition)
        for i in range(0, len(positions)):
            for alterpos in spacerem:

                alter_position = copy.deepcopy(new_positions)

                alter_position[i] = alterpos

                temp_score, temp_map = evaluate.evaluate(mymap,
                                                         alter_position, toxic,
                                                         scenic,
                                                         indu, comm, resi, Nx,
                                                         Ny)

                if temp_score > newscore:
                    newscore = temp_score
                    realmap1 = copy.deepcopy(temp_map)
                    realposition1 = copy.deepcopy(alter_position)
                # print(realposition1, alter_position, iteration, temp_score,
                #       newscore)

        realposition = copy.deepcopy(realposition1)
        # print(realposition, iteration)
        spacerem = copy.deepcopy(randomseed)
        for removepos in realposition:
            spacerem.remove(removepos)
        if newscore > score:
            score = newscore
            finalmap = copy.deepcopy(realmap1)
            finaltime = time.time() - start_time
        if(time.time() - start_time >= deadline):
            break


print("--- %s seconds ---" % (time.time() - start_time))  # time counter
print(score, '\n', finalmap, '\n', finaltime)

# with open('answer.txt', 'wt') as f:
#     f.write('X,1,2,3''\n')
#     f.w
#     # f.write(1)
print(score, file=open("output.txt", "a"))
print(finaltime, file=open("output.txt", "a"))
for i in range(0, len(finalmap)):
    print(finalmap[i], file=open("output.txt", "a"))

print(iteration, iteration1)
