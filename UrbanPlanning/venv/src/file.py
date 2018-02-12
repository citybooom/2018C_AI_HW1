def read_input():
    result = []
    map = []
    file_name = "sample 2.txt"
    mode = "r"
    with open(file_name, mode) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if cnt == 1:
                i = int(line)
                result.append(i)
            if cnt == 2:
                r = int(line)
                result.append(r)
            if cnt == 3:
                c = int(line)
                result.append(c)
            if cnt >= 4:
                map_line = line.strip().split(",")
                map.append(map_line)
            line = fp.readline()
            cnt += 1
        result.append(map)
        # print (result)
    return result


def get_industrial(file_input):
    # type: (object) -> object
    return file_input[0]


def get_residential(file_input):
    return file_input[1]


def get_commercial(file_input):
    return file_input[2]


def get_map(file_input):
    urban_map = file_input[3]
    return urban_map


def save_output(urban_map, file_name):
    output_file = open(file_name, 'w')

    for i in range(len(urban_map)):
        output_file.write(str(urban_map[i]) + '\n')

    output_file.close()