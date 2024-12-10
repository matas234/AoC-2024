
from typing import List, Tuple


def get_data() -> Tuple[List[str], int, int, int]:
    with open("input6.txt") as f:
        data = f.read().strip()

    num_rows = len(data.split("\n"))
    row_size = len(data.split("\n")[0])

    data = data.replace("\n", "")
    start = data.find("^")

    data = "".join(data)

    return list(data), \
           num_rows, \
           row_size, \
           start


## UP = 0, RIGHT = 1, DOWN = 2, LEFT = 3

def next_move(dir:      int,
              idx:      int,
              row_size: int
              ) -> int:

    if dir == 0:
        return idx - row_size

    elif dir == 1:
        return idx + 1

    elif dir == 2:
        return idx + row_size

    elif dir == 3:
        return idx - 1



def is_on_edge(idx:      int,
               row_size: int,
               num_rows: int
               ) -> bool:


    return idx % row_size == 0 or \
           idx % row_size == row_size - 1 or \
           idx // row_size == 0 or \
           idx // row_size == num_rows - 1



def part1():
    direction = 0

    data, num_rows, row_size, cur = get_data()

    visited = {cur}

    while not is_on_edge(cur, row_size, num_rows):


        if data[next := next_move(direction, cur, row_size)] == '#':
            direction = (direction + 1) % 4
            continue

        visited.add(cur)
        cur = next

    return len(visited) + 1







def check_for_loop_at_next_idx(idx:      int,
                               dir:      int,
                               data:     List[str],
                               row_size: int,
                               num_rows: int
                               ) -> bool:


    next_idx = next_move(dir, idx, row_size)
    data[next_idx] == '#'

    dir = (dir + 1) % 4


    visited = {(idx, dir)}
    cur = idx

    while not is_on_edge(cur, row_size, num_rows):
        if data[next := next_move(dir, cur, row_size)] == '#':
            dir = (dir + 1) % 4
            continue

        cur = next

        if (cur, dir) in visited:
            data[next] = '.'
            return True

        visited.add((cur, dir))

    data[next] = '.'
    return False





def part2():
    data, num_rows, row_size, cur = get_data()
    added_walls = {cur}
    dir = 0

    while not is_on_edge(cur, row_size, num_rows):
        if data[next := next_move(dir, cur, row_size)] == '#':
            dir = (dir + 1) % 4
            continue

        else:
            if check_for_loop_at_next_idx(cur, dir, data, row_size, num_rows):
                added_walls.add(next)

            cur = next


    return len(added_walls) - 1









print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
