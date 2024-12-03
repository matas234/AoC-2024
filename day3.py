



import re
import time


start = time.time()

string = open('input.txt', 'r').read()


pattern = r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)"
match_iter = re.finditer(pattern, string)

is_enabled = True
out = 0

for match in match_iter:
    if match.group() == 'do()':
        is_enabled = True

    elif match.group() == "don't()":
        is_enabled = False

    elif is_enabled:
        out += int(match.group(1)) * int(match.group(2))

print(time.time() - start)
print(out)
