from file import *
from section import *
from plan import *
import datetime


def main():
    global final_bonus, final_population_state, population, elitism_target
    # Run urban planning problem using generic algorithm
    # read input file
    start_time = datetime.datetime.now()
    print (start_time)
    end_time = start_time + datetime.timedelta(seconds=1)
    print (end_time)
    file_input = read_input()
    i = get_industrial(file_input)
    r = get_residential(file_input)
    c = get_commercial(file_input)
    urban_map = get_map(file_input)

    population_num = 100
    population = get_population(i, r, c, urban_map, population_num)

    final_population_state = population[0]
    final_bonus = float('-inf')
    while end_time > datetime.datetime.now():
        fitness_rank = get_all_fitness(i, r, c, population, urban_map)
        if fitness_rank[0][0] > final_bonus:
            final_population_state = deepcopy(fitness_rank.__getitem__(0))
        final_bonus = max(final_bonus, fitness_rank[0][0])
        ranked_population = get_ranked_population(fitness_rank)

        elitism_target = elitism(fitness_rank)[1]
        culling_target = culling(fitness_rank)[1]

        ranked_population.remove(culling_target)
        # plan
        population = selection_crossover(deepcopy(ranked_population), len(urban_map[0]) * len(urban_map))
        population = mutation(population, len(urban_map[0]) * len(urban_map))
        population.append(elitism_target)
        print (final_bonus)
    print (final_bonus)
    print (final_population_state)
    print (datetime.datetime.now())

    # output result
    # save_output(get_final_map(i, r, c, final_population_state[1], urban_map), "final_map.txt")
    # print (urban_map)
    # print (get_final_map(i, r, c, final_population_state[1], urban_map))


if __name__ == '__main__':
    main()
