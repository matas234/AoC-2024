from collections import defaultdict
import itertools


with open('input8.txt', 'r') as f:
    data = f.read().strip().split('\n')



def get_antinodes(loc1, loc2):
    diff = (loc1[0] - loc2[0], loc1[1] - loc2[1])

    return (loc1[0] + diff[0], loc1[1] + diff[1]), \
           (loc2[0] - diff[0], loc2[1] - diff[1])


def in_bounds(loc):
    return 0 <= loc[0] < len(data) and 0 <= loc[1] < len(data[0])



def part1():
    freq_to_loc = defaultdict(list)

    for line_idx, line in enumerate(data):
        for char_idx, char in enumerate(line):
            if char != '.':
                freq_to_loc[char].append((line_idx, char_idx))


    unique_locs = set()

    for freq, locs in freq_to_loc.items():
        for loc1, loc2 in itertools.combinations(locs, 2):

            for antinode in get_antinodes(loc1, loc2):
                if in_bounds(antinode):
                    unique_locs.add(antinode)

    return len(unique_locs)



print(f"Part 1: {part1()}")


def get_antinodes2(loc1, loc2):
    diff = (loc1[0] - loc2[0], loc1[1] - loc2[1])

    for offset in range(max(len(data), len(data[0]))):
        yield (loc1[0] + offset * diff[0], loc1[1] + offset * diff[1])
        yield (loc2[0] - offset * diff[0], loc2[1] - offset * diff[1])


def part2():
    freq_to_loc = defaultdict(list)

    for line_idx, line in enumerate(data):
        for char_idx, char in enumerate(line):
            if char != '.':
                freq_to_loc[char].append((line_idx, char_idx))


    unique_locs = set()

    for freq, locs in freq_to_loc.items():
        for loc1, loc2 in itertools.combinations(locs, 2):

            for antinode in get_antinodes2(loc1, loc2):
                if in_bounds(antinode):
                    unique_locs.add(antinode)

    return len(unique_locs)


print(f"Part 2: {part2()}")
