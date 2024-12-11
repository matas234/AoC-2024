from collections import Counter

with open('input11.txt', 'r') as f:
    stones = Counter(map(int,f.read().strip().split(' ')))


def grow_stones(num_of_blinks):
    cur_stones = stones

    for _ in range(num_of_blinks):
        new_stones = Counter()

        for n, num_stones in cur_stones.items():
            mid, rem = divmod(len(str(n)), 2)

            if n == 0:
                new_stones[1] += num_stones

            elif rem:
                new_stones[n * 2024] += num_stones

            else:
                for split_stone in divmod(n, 10**mid):
                    new_stones[split_stone] += num_stones

        cur_stones = new_stones

    return sum(cur_stones.values())

print(f"Part 1: {grow_stones(25)}")
print(f"Part 2: {grow_stones(75)}")
