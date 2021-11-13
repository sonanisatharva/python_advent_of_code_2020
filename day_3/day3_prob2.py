with open('input.txt') as f:
    lines = f.readlines()
map = [str(line.strip()) for line in lines]


width = 32

def find_trees(down, right):
    trees = 0
    row, column = 0,0
    while row + 1 < len(map):
        # print("Row", row)
        # print(len(map))
        row += right
        column += down
        space = map[row][column % len(map[row])]
        if space == '#':
            trees += 1

    return trees

trees_1 = find_trees(1,1)
trees_2 = find_trees(3,1)
trees_3 = find_trees(5,1)
trees_4 = find_trees(7,1)
trees_5 = find_trees(1,2)
f_m_trees = trees_1 * trees_2 * trees_3 * trees_4 * trees_5

print(f_m_trees)
