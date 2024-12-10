from collections import defaultdict
import time


with open('input9.txt', 'r') as f:
    data = f.read().strip()


def part1():
    files, empty = [], []

    cur_id = 0
    is_file = True

    formated = []
    ptr = 0

    for num in data:
        if is_file:
            formated += [cur_id] * int(num)
            cur_id += 1

        else:
            formated += ['.'] * int(num)

        ptr += int(num)
        is_file = not is_file


    file_ptr = len(formated) - 1
    empty_ptr = 0

    while (file_ptr >= 0 and empty_ptr < len(formated)) and empty_ptr < file_ptr:
        if formated[file_ptr] == '.':
            file_ptr -= 1
            continue

        if formated[empty_ptr] != '.':
            empty_ptr += 1
            continue


        idx_to_move = formated[file_ptr]
        formated[file_ptr] = '.'
        formated[empty_ptr] = idx_to_move


    out = 0
    for idx, id in enumerate(formated):
        if id == '.':
            break

        out += id * idx


    return out


print(f"Part 1: {part1()}")



def part2():
    cur_id = 0
    is_file = True

    formated = []
    ptr = 0

    for num in data:
        if is_file:
            formated += [[cur_id] * int(num)]
            cur_id += 1

        else:
            formated += [['.'] * int(num)]

        ptr += int(num)
        is_file = not is_file


    file_idx = len(formated) - 1

    while file_idx > 0:
        file = formated[file_idx]
        empty_idx = 1

        while empty_idx < file_idx:

            if len(formated[empty_idx]) >= len(file):
                formated[empty_idx] = formated[empty_idx][: -len(file)]
                formated[file_idx] = ['.'] * len(file)

                formated.insert(empty_idx, file)
                formated.insert(empty_idx, [])

                file_idx += 2

                break

            empty_idx += 2

        file_idx -= 2


    out, idx = 0, 0
    for file_idx, file in enumerate(formated):
        l = len(file)

        if file_idx % 2 == 0 and l and file[0] != '.':
            v = file[0]

            out += v * l * (2 * idx + l - 1) // 2

        idx += l

    return out



start = time.time()

print(f"Part 2: {part2()}")

print(f"Time: {time.time() - start}")
