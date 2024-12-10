with open('input10.txt', 'r') as f:
    data = f.read().strip().split('\n')


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs_part1(x, y, locs_of_nines, depth = 1):
    if depth == 10 and (x, y) not in locs_of_nines:
        locs_of_nines.add((x, y))
        return 1


    return sum(
        dfs_part1(x + dx, y + dy, locs_of_nines, depth + 1)
        for dx, dy in dirs
        if 0 <= x + dx < len(data)
        and 0 <= y + dy < len(data[0])
        and data[x + dx][y + dy] == str(depth)
        )




def part1():
    sum = 0

    for x in range(len(data)):
        for y in range(len(data[0])):

            if data[x][y] == '0':
                sum += dfs_part1(x, y, set())

    return sum

print(f"Part 1: {part1()}")



def dfs_part2(x, y, depth = 1):
    if depth == 10:
        return 1


    return sum(
        dfs_part2(x + dx, y + dy, depth + 1)
        for dx, dy in dirs
        if 0 <= x + dx < len(data)
        and 0 <= y + dy < len(data[0])
        and data[x + dx][y + dy] == str(depth)
        )


def part2():
    sum = 0

    for x in range(len(data)):
        for y in range(len(data[0])):

            if data[x][y] == '0':
                sum += dfs_part2(x, y)

    return sum

print(f"Part 2: {part2()}")
