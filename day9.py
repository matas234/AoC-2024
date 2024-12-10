from collections import Counter, defaultdict, deque
import time


with open('input9.txt', 'r') as f:
    data = f.read().strip()


def part1():
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
    len_formated = len(formated)

    while (file_ptr >= 0 and empty_ptr < len_formated) and empty_ptr < file_ptr:
        if formated[file_ptr] == '.':
            file_ptr -= 1
            continue

        if formated[empty_ptr] != '.':
            empty_ptr += 1
            continue


        idx_to_move = formated[file_ptr]
        formated[file_ptr] = '.'
        formated[empty_ptr] = idx_to_move


    checksum = 0
    for idx, id in enumerate(formated):
        if id == '.':
            break

        checksum += id * idx


    return checksum

start = time.time()
print(f"Part 1: {part1()}")
print(f"Time: {time.time() - start}")



def get_formatted():
    cur_id, ptr = 0, 0;  is_file = True;  formated = []

    for num in data:
        num = int(num)
        if is_file:
            formated.append((cur_id, num))
            cur_id += 1
        else:
            formated.append(num)

        ptr += num
        is_file = not is_file


    return formated



def part2():
    # alternating list of tuple, int, tuple, ...
    # where tuple = (id, len) which denotes information about a file
    # and int is the length of the empty space
    formated = get_formatted()

    file_idx = len(formated) - 1

    while file_idx > 0:
        cur_id, file_len = formated[file_idx]

        for empty_idx in range(1, file_idx, 2):

            if formated[empty_idx] >= file_len:

                formated[empty_idx] -= file_len
                formated[file_idx] = (0, file_len)

                formated.insert(empty_idx, (cur_id, file_len))
                formated.insert(empty_idx, 0)
                ## 2 values got inserted before file_idx, so not increasing file_idx is the same
                ## as decreasing it by 2 in the old list (going to the next file)
                break

        else:
            # nothing happened so go to the next file
            file_idx -= 2


    checksum, idx = 0, 0
    for file_idx, file in enumerate(formated):

        if file_idx % 2 == 0:
            cur_id, file_len = file

            ## formula is for cur_id * (sum of consecutive numbers form idx to (idx + file_len - 1 ))
            checksum += cur_id * file_len * (2*idx + file_len - 1) // 2
            idx += file_len

        else:
            idx += file

    return checksum



start = time.time()

print(f"Part 2: {part2()}")

print(f"Time: {time.time() - start}")
