import random
from copy import copy, deepcopy
from section import *


def get_population(i, r, c, urban_map, count):
    range_max = urban_map.__len__() * urban_map[0].__len__()

    result = []
    for x in range(count):
        result_x = random.sample(xrange(1, range_max + 1), i + r + c)
        while result.__contains__(result_x):
            result_x = random.sample(xrange(1, range_max + 1), i + r + c)
        result.append(result_x)
    # result.sort()
    return result


def get_all_fitness(i, r, c, states, urban_map):
    result = []
    for x in range(len(states)):
        final_urban_map = get_final_map(i, r, c, states[x], urban_map)
        fitness = get_fitness(i, r, c, states[x], urban_map, final_urban_map)
        result.append((fitness, states[x]))
    result.sort(reverse=True)

    return result


def get_ranked_population(fitness_result):
    result = []
    for i in range(len(fitness_result)):
        result.append(fitness_result[i][1])
    return result


def get_final_map(i, r, c, population, urban_map):
    final_urban_map = deepcopy(urban_map)
    for x in range(population.__len__()):
        target_row = population[x] / urban_map[0].__len__()
        target_col = population[x] % urban_map[0].__len__()
        if target_col == 0:
            target_col = urban_map[0].__len__()
        else:
            target_row += 1

        if x < i:
            final_urban_map[target_row - 1][target_col - 1] = 'I'
        elif x < i + r:
            final_urban_map[target_row - 1][target_col - 1] = 'R'
        elif x < i + r + c:
            final_urban_map[target_row - 1][target_col - 1] = 'C'
    return final_urban_map


def selection_crossover(population, index_range):
    for x in range(population.__len__() // 2):
        selection_point = random.randint(1, len(population[x]) - 1)
        temp_1 = population[2*x][selection_point:]
        temp_2 = population[2*x + 1][selection_point:]
        del population[2*x][selection_point:]
        del population[2*x + 1][selection_point:]

        for i in range(len(temp_1)):
            while (temp_1[i] in population[2*x + 1]) or len(set([m for m in temp_1 if temp_1.count(m) > 1])) != 0:
                if temp_1[i] == 1:
                    temp_1[i] = temp_1[i] + 1
                elif temp_1[i] == index_range:
                    temp_1[i] = temp_1[i] - 1
                else:
                    temp_1[i] = temp_1[i] + random.choice([-1, 1])
            while (temp_2[i] in population[2*x]) or len(set([n for n in temp_2 if temp_2.count(n) > 1])) != 0:
                if temp_2[i] == 1:
                    temp_2[i] = temp_2[i] + 1
                elif temp_2[i] == index_range:
                    temp_2[i] = temp_2[i] - 1
                else:
                    temp_2[i] = temp_2[i] + random.choice([-1, 1])

        population[2 * x] = population[2 * x] + temp_2
        population[2 * x + 1] = population[2 * x + 1] + temp_1
    return population


def elitism(fitness_rank):
    return fitness_rank[0]


def culling(fitness_rank):
    fitness_rank.sort()
    return fitness_rank[0]


def mutation(sub_population, target_range):
    for x in range(sub_population.__len__()):
        mutate_index = random.randint(1, len(sub_population[x]))
        mutate_target = random.randint(1, target_range)
        while mutate_target in sub_population[x]:
            mutate_target = random.randint(1, target_range)
        sub_population[x][mutate_index - 1] = mutate_target
    return sub_population
