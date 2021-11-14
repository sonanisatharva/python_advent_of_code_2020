
def is_passport_valid(passport):
    for field in fields:
        if field not in passport:
            return False
    return True

with open('input.txt') as f:
    lines = f.readlines()
input = [(line.strip('\n')) for line in lines]
# print(input)

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = 0

cp = ''
for line in input:
    if line != '':
        cp += '' + line
    else:
        if is_passport_valid(cp):
            valid += 1
        cp = ''
if is_passport_valid(cp):
    valid +=1

print(valid)
