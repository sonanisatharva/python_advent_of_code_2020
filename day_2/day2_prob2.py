with open('input.txt') as f:
    lines = f.readlines()
n = [str(line.strip()) for line in lines]
answer = 0
for i in n:
    first, password = i.split(':')
    f,letter = first.split()
    num1, num2 = f.split('-')
    if ((password[int(num1)]== letter) ^ (password[int(num2)]== letter)):
        answer += 1

print(answer)
