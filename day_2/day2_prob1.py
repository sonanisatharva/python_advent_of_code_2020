with open('input.txt') as f:
    lines = f.readlines()
n = [str(line.strip()) for line in lines]
answer = 0
for i in n:
    first, second = i.split(':')
    f,letter = first.split()
    num1, num2 = f.split('-')
    count = 0
    for i in second:
        if (i == letter):
            count += 1
    if (int(num1) <= count <= int(num2)):
        answer += 1
print('ANSWER = ', answer)
