# get fitness of industrial, residential, commercial
def get_fitness(i, r, c, state, urban_map, final_urban_map):
    i_fitness = 0
    for x in range(i):
        i_fitness += get_industrial_fitness(x, state, urban_map, final_urban_map)

    r_fitness = 0
    for y in range(r):
        r_fitness += get_residential_fitness(y + i, state, urban_map, final_urban_map)

    c_fitness = 0
    for z in range(c):
        c_fitness += get_commercial_fitness(z + i + r, state, urban_map, final_urban_map)

    return i_fitness + r_fitness + c_fitness


# get industrial fitness
def get_industrial_fitness(n, state, urban_map, final_urban_map):
    row_position = state[n] / urban_map[0].__len__()
    col_position = state[n] % urban_map[0].__len__()
    if col_position == 0:
        col_position = urban_map[0].__len__()
    else:
        row_position += 1
    bonus = get_industrial_bonus(row_position - 1, col_position - 1, final_urban_map)
    penalty = get_industrial_penalty(row_position - 1, col_position - 1, urban_map, final_urban_map)

    return bonus - penalty


# get residential fitness
def get_residential_fitness(n, state, urban_map, final_urban_map):
    row_position = state[n] / urban_map[0].__len__()
    col_position = state[n] % urban_map[0].__len__()
    if col_position == 0:
        col_position = urban_map[0].__len__()
    else:
        row_position += 1
    bonus = get_residential_bonus(row_position - 1, col_position - 1, final_urban_map)
    penalty = get_residential_penalty(row_position - 1, col_position - 1, urban_map, final_urban_map)

    return bonus - penalty


# get commercial fitness
def get_commercial_fitness(n, state, urban_map, final_urban_map):
    row_position = state[n] / urban_map[0].__len__()
    col_position = state[n] % urban_map[0].__len__()
    if col_position == 0:
        col_position = urban_map[0].__len__()
    else:
        row_position += 1
    bonus = get_commercial_bonus(row_position - 1, col_position - 1, final_urban_map)
    penalty = get_commercial_penalty(row_position - 1, col_position - 1, urban_map, final_urban_map)

    return bonus - penalty


# get industrial bonus
def get_industrial_bonus(row, col, final_urban_map):
    industrial_bonus = 3
    industrial_count = count_section(row, col, 2, final_urban_map, 'I') - 1
    bonus = industrial_count * industrial_bonus

    return bonus


# get industrial penalty
def get_industrial_penalty(row, col, urban_map, final_urban_map):
    penalty = get_build_penalty(row, col, urban_map)

    x_penalty = 10
    x_count = count_section(row, col, 2, final_urban_map, 'X')
    penalty += x_count * x_penalty

    return penalty


# get residential bonus
def get_residential_bonus(row, col, final_urban_map):
    s_bonus = 10
    s_count = count_section(row, col, 2, final_urban_map, 'S')
    bonus = s_count * s_bonus

    c_bonus = 5
    c_count = count_section(row, col, 3, final_urban_map, 'C')
    bonus += c_count * c_bonus

    return bonus


# get residential penalty
def get_residential_penalty(row, col, urban_map, final_urban_map):
    penalty = get_build_penalty(row, col, urban_map)

    x_penalty = 20
    x_count = count_section(row, col, 2, final_urban_map, 'X')
    penalty += x_count * x_penalty

    i_penalty = 5
    i_count = count_section(row, col, 3, final_urban_map, 'I')
    penalty += i_count * i_penalty

    return penalty


# get commercial bonus
def get_commercial_bonus(row, col, final_urban_map):
    r_bonus = 5
    r_count = count_section(row, col, 3, final_urban_map, 'R')
    bonus = r_count * r_bonus

    return bonus


# get commercial penalty
def get_commercial_penalty(row, col, urban_map, final_urban_map):
    penalty = get_build_penalty(row, col, urban_map)

    x_penalty = 20
    x_count = count_section(row, col, 2, final_urban_map, 'X')
    penalty += x_count * x_penalty

    c_penalty = 5
    c_count = count_section(row, col, 2, final_urban_map, 'C') - 1
    penalty += c_count * c_penalty

    return penalty


# get build penalty for 3 sections
def get_build_penalty(row, col, urban_map):
    penalty = 0
    if is_x(row, col, urban_map):
        penalty += float('inf')
    elif is_s(row, col, urban_map):
        penalty += 0
    else:
        penalty += int(urban_map[row][col])

    return penalty


# count section within steps
def count_section(row, col, step, final_urban_map, section_type):
    count = 0
    for i in range(row - step, row + step, 1):
        for j in range(col - step, col + step, 1):
            if 0 <= i <= final_urban_map.__len__() - 1 and 0 <= j <= final_urban_map[0].__len__() - 1 and (abs(row - i) + abs(col - j)) <= step:
                if final_urban_map[i][j] == section_type:
                    count += 1
                else:
                    continue
    return count


def is_industrial(row, col, final_urban_map):
    if in_map(row, col, final_urban_map.__len__() - 1, final_urban_map[0].__len__() - 1):
        section = final_urban_map[row][col]
        if section == 'I':
            return true
        else:
            return false
    else:
        return false


def is_residential(row, col, final_urban_map):
    if in_map(row, col, final_urban_map.__len__() - 1, final_urban_map[0].__len__() - 1):
        section = final_urban_map[row][col]
        if section == 'R':
            return true
        else:
            return false
    else:
        return false


def is_commercial(row, col, final_urban_map):
    if in_map(row, col, final_urban_map.__len__() - 1, final_urban_map[0].__len__() - 1):
        section = final_urban_map[row][col]
        if section == 'C':
            return True
        else:
            return False
    else:
        return False


def is_x(row, col, final_urban_map):
    if in_map(row, col, final_urban_map.__len__() - 1, final_urban_map[0].__len__() - 1):
        section = final_urban_map[row][col]
        if section == 'X':
            return True
        else:
            return False
    else:
        return False


def is_s(row, col, final_urban_map):
    if in_map(row, col, final_urban_map.__len__() - 1, final_urban_map[0].__len__() - 1):
        section = final_urban_map[row][col]
        if section == 'S':
            return True
        else:
            return False
    else:
        return False


def in_map(row, col, total_row, total_col):
    if 0 <= row <= total_row and 0 <= col <= total_col:
        return True
    else:
        return False
