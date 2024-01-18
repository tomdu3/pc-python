# Longest Consecutive Sequence: Create a function that finds the length of the longest consecutive elements sequence in an unsorted list.

def longest_consec_seq(nums):
    longest_seq = 0
    current_seq = 1
    for i in range(len(nums)-1):
        if nums[i] + 1 == nums[i+1]:
            current_seq += 1
        else:
            longest_seq = max(longest_seq, current_seq)
            current_seq = 1
    return longest_seq

nums = [1,2,10,11,4,7,100,101,106]

print(longest_consec_seq(nums))
        
