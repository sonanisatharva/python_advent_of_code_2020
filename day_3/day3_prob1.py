with open('input.txt') as f:
    lines = f.readlines()
map = [str(line.strip()) for line in lines]

trees = 0
width = 32
line_number = 0

row, column = 0,0

while row + 1 < len(map):
    # print("Row", row)
    # print(len(map))

    row += 1
    column += 3

    space = map[row][column % len(map[row])]
    if space == '#':
        trees += 1
    print('- - - - - - -- - - ')
    print('row', row)
    print("COLUMN", column)
    print('len(map[row])',len(map[row]))
    print('Space', space)
    print('- - - - - - - - - ')
# for line in n:
#     # print(line)
#     count = 0
#     condition = 'a'
#     line_number += 1
#     if ( condition == 'a'):
#         count += 3
#         print('hello a, changing count by adding 3')
#         if (count >= width):
#             count = 0
#         condition = 'b'
#
#     if ( condition == 'b'):
#         print('hello b, checking the 1 down value')
#         if ( line[count] == '#'):
#             trees += 1
#             print("Tree Added !!!!!!! AT line", line_number + 1)
#         if (count >= width):
#             count = 0
#         condition = 'a'


print('Trees Dashed =',trees )
