data = [line.strip() for line in open('input4.txt', 'r')]

data_x_len = len(data)
data_y_len = len(data[0])


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)]


## PART 1
count = 0
for x in range(data_x_len):
    for y in range(data_y_len):

        if data[x][y] == 'X':

            for dx, dy in dirs:

                path = [(x + i*dy, y + i*dx)
                        for i in range(1, 4)
                        if  0 <= x + i*dy < data_x_len
                        and 0 <= y + i*dx < data_y_len
                        ]

                string_on_path = ''.join(data[ p[0] ][ p[1] ] for p in path)

                if string_on_path == 'MAS':
                    count += 1


print(f"Part 1: {count}")



## PART 2


#         M → M   S → S   S → M   M → S
#           A ↓     A ↓     A ↓     A ↓
#         S ← S   M ← M   S ← M   M ← S
TARGET = {'MMSS', 'SSMM', 'SMMS', 'MSSM'}

diag_dirs = ((-1,-1), (-1,1), (1,1), (1,-1))

count = 0

for x in range(1, data_x_len-1):
    for y in range(1, data_y_len-1):

        if data[x][y] == 'A':
            new_string = ''.join(data[x+dx][y+dy] for dx, dy in diag_dirs)

            if new_string in TARGET:
                count += 1




print(f"Part 2: {count}")
