from typing import List


with open('input7.txt') as f:
    data = f.read().strip().split('\n')

targets, equations = zip(
    *[
        (int(line.split(':')[0]),
        list(map(int, line.split(':')[1].strip().split(' ')))
        )
        for line in data
    ]
)


## part 1
def search(target:   int,
           equation: List[int],
           depth = 1,
           running_total = None
           ) -> bool:

    if running_total is None:
        running_total = equation[0]

    if depth == len(equation):
        return running_total == target

    if running_total > target:
        return False

    return search(target, equation, depth + 1, running_total + equation[depth]) or \
           search(target, equation, depth + 1, running_total * equation[depth])


part_1 = sum(
    target
    for target, equation in zip(targets, equations)
    if search(target, equation)
)

print(f"Part 1: {part_1}")




## part 2
def search2(target:   int,
           equation: List[int],
           depth = 1,
           running_total = None
           ) -> bool:

    if running_total is None:
        running_total = equation[0]

    if depth == len(equation):
        return running_total == target

    if running_total > target:
        return False

    return search2(target, equation, depth + 1, running_total + equation[depth]) or \
           search2(target, equation, depth + 1, running_total * equation[depth]) or \
           search2(target, equation, depth + 1, int(str(running_total) + str(equation[depth])))


part_2 = sum(
    target
    for target, equation in zip(targets, equations)
    if search(target, equation)
    or search2(target, equation)
)

print(f"Part 2: {part_2}")
