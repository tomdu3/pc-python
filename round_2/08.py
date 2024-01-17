# Two-Sum Problem: Develop a function that takes a list of numbers and a target
# sum, returning the indices of the two numbers that add up to the target sum.

def two_sum(nums, target):
    indices = []
    numbers = {}
    for i, num in enumerate(nums):
        if target-num in nums:
            if num not in numbers:
                numbers[num] = i
    for key in numbers.keys():
        if sorted([numbers[key], numbers[target-key]]) in indices or numbers[key] == numbers[target-key]:
            continue
        else:
            indices.append(sorted([numbers[key], numbers[target-key]]))
    return indices

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

print(two_sum(nums, 20))
