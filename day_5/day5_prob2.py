with open('input.txt') as f:
    lines = f.readlines()
input = [(line.strip('\n')) for line in lines]
# print(input)

def row(seat):
    l , h = 0 , 127
    for i in range(6):
        m = (l+h)//2
        if seat[i] == 'F':
            h = m
        elif seat[i] == 'B':
            l = m + 1
    if seat[6] == 'F':
        return l
    else:
        return h

def column(seat):
    l , h = 0 , 7
    for i in range(2):
        m = (l+h)//2
        if seat[i] == 'L':
            h = m
        elif seat[i] == 'R':
            l = m + 1
    if seat[2] == 'L':
        return l
    else:
        return h

largest = -1
seat_id = []
rrow = []
ccol = []
for i in input:
    r = row(i[:7])
    rrow.append(r)
    c = column(i[7:])
    ccol.append(c)
    id = r * 8 + c
    seat_id.append(id)
    if id > largest:
        largest = id

# print(largest)
sort_seat_id = sorted(seat_id)
# print(sorted(rrow))
# print(ccol)
# print(sort_seat_id)

prev = 0
missing = []
for p in sort_seat_id:
    if (prev != p -1):
        missing.append(p-1)
    prev = p

print(missing)
