
import re


string = open('input3.txt', 'r').read()


### PART 1
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
match_iter = re.finditer(pattern, string)

out = 0

for match in match_iter:
    out += int(match.group(1)) * int(match.group(2))

print(f"Part 1: {out}")





### PART 2
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


print(f"Part 2: {out}")
