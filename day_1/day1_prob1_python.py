with open('input.txt') as f:
    lines = f.readlines()

# print(lines)
nums = [ int(line.strip()) for line in lines ]
# print(nums)

largest_answer = -1

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        n1 = nums[i]
        n2 = nums[j]

        if n1 + n2 == 2020:
            answer = n1 * n2

            if answer > largest_answer:
                largest_answer = answer

print("Answer = ", largest_answer)
