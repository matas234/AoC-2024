def is_safe(line):
    is_increasing = 1 if line[1] > line[0] else -1

    return all(1 <= is_increasing * (line[i] - line[i-1]) <= 3
               for i in range(1, len(line)))


### PART 1
count = 0
with open('input2.txt', 'r') as f:
    for line in f:
        line = list(map(int, line.strip().split(' ')))

        if is_safe(line):
            count += 1


print(f"Part 1: {count}")


### PART 2
count = 0

with open('input2.txt', 'r') as f:
    for line in f:
        line = list(map(int, line.strip().split(' ')))

        if (is_safe(line) or
            any(is_safe(line[:i] + line[i+1:])
                for i in range(len(line)))
            ):
            count += 1


print(f"Part 2: {count}")
