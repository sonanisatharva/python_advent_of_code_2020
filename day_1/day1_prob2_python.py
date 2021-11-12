with open('input.txt') as f:
    lines = f.readlines()

# print(lines)
nums = [ int(line.strip()) for line in lines ]
# print(nums)

largest_answer = -1

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        for k in range(j + 1, len(nums)):
            n1 = nums[i]
            n2 = nums[j]
            n3 = nums[k]

            if n1 + n2 + n3 == 2020:
                answer = n1 * n2 * n3

                if answer > largest_answer:
                    largest_answer = answer

print("Answer = ", largest_answer)
