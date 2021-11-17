with open('input.txt') as f:
    lines = f.readlines()
input = [(line.strip('\n')) for line in lines]
print(input)

def f_letter():

def seat_id(i):
    return i * 8 + 5

h_seat = -1

for seat in input:
    row, column = seat[0:7] , seat[7:]
