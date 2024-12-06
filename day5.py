from collections import defaultdict
import time
from typing import List, Tuple


data = open('input5.txt', 'r').read()


rules, updates = data.strip().split('\n\n')


updates = updates.split('\n')
rules   =   rules.split('\n')


updates = list(
    map(
        lambda s: list(map(int, s.strip().split(','))),
        updates
    )
)

rules = list(
    map(
        lambda s: list(map(int, s.strip().split('|'))),
        rules
    )
)



### part 1
def correctly_ordered_updates():
    page_to_exceptions = defaultdict(set)

    for rule in rules:
        page_to_exceptions[rule[1]].add(rule[0])


    for update in updates:
        curent_exceptions = set()

        for page in update:
            if page in curent_exceptions:
                break
            curent_exceptions.update(page_to_exceptions[page])
        else:
            yield update



start = time.time()
count = 0

for update in correctly_ordered_updates():
    count += update[ len(update) // 2 ]

print(time.time() - start)

print(f"Part 1: {count}")


### PART 2

page_to_exceptions = defaultdict(set)
for rule in rules:
    page_to_exceptions[rule[1]].add(rule[0])



def is_incorrectly_ordered_updates(update: List[int],
                                   has_updated = False
                                   ) -> List[int] | None:
    curent_exceptions = set()
    exception_to_idx = {}

    for cur_idx, page in enumerate(update):
        if page in curent_exceptions:

            idx_of_exception = exception_to_idx[page]

            update[cur_idx]          = update[idx_of_exception]
            update[idx_of_exception] = page

            return is_incorrectly_ordered_updates(update, True)

        curent_exceptions.update(page_to_exceptions[page])

        for exception in page_to_exceptions[page]:
            exception_to_idx[exception] = cur_idx


    if has_updated:
        return update


start = time.time()
count = 0
for update in updates:
    corrected_update = is_incorrectly_ordered_updates(update)
    if corrected_update:
        count += corrected_update[ len(corrected_update) // 2 ]

print(time.time() - start)
print(f"Part 2: {count}")
