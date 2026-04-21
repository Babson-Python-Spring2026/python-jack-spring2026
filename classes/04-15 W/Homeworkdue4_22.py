
#State:
#The input state is the list nums, which is a list of integers. The list itself does not change during the problem. While solving the problem, the algorithm also keeps track of information about the runs it finds so it can return the correct dictionary at the end.

#Transitions:
#There are no transitions in the input state itself because nums is never modified. The list stays the same from start to finish. The program only reads the values in the list and compares adjacent numbers to determine whether they form increasing runs, decreasing runs, or no run at all.

#Invariants:
# Any run must be contiguous, meaning the values must be next to each other in the list.  Any increasing run must be strictly increasing.    Any decreasing run must be strictly decreasing.     The function must return the dictionary in the required format

#Assumptions & Edge Cases:
#I am assuming that run length means the number of elements in the run, not the size of the increase or decrease. I am also assuming that a valid increasing or decreasing run must have at least two elements. Equal adjacent values break runs. If there is a tie for the longest run, either tied run can be returned. If there are no valid increasing or decreasing runs, the function should still return the required dictionary with zero counts and an empty list for longest_run_values.


def longest_increasing_run(nums):
    if len(nums) < 2:
        return 0

    longest = 0
    current = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1

    return longest

def longest_decreasing_run(nums):
    if len(nums) < 2:
        return 0

    longest = 0
    current = 1

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1

    return longest

def num_increasing_runs(nums):
    count = 0
    current = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current += 1
        else:
            if current >= 2:
                count += 1
            current = 1

    if current >= 2:
        count += 1

    return count

def num_decreasing_runs(nums):
    count = 0
    current = 1

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            current += 1
        else:
            if current >= 2:
                count += 1
            current = 1

    if current >= 2:
        count += 1

    return count

def longest_run_values(nums):
    if len(nums) < 2:
        return []

    longest_inc = []
    current_inc = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_inc.append(nums[i])
        else:
            if len(current_inc) >= 2 and len(current_inc) > len(longest_inc):
                longest_inc = current_inc
            current_inc = [nums[i]]

    if len(current_inc) >= 2 and len(current_inc) > len(longest_inc):
        longest_inc = current_inc

    longest_dec = []
    current_dec = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            current_dec.append(nums[i])
        else:
            if len(current_dec) >= 2 and len(current_dec) > len(longest_dec):
                longest_dec = current_dec
            current_dec = [nums[i]]

    if len(current_dec) >= 2 and len(current_dec) > len(longest_dec):
        longest_dec = current_dec

    if len(longest_inc) >= len(longest_dec):
        return longest_inc
    else:
        return longest_dec

def analyze_runs(nums):
    return {
        "longest_increasing_run": longest_increasing_run(nums),
        "longest_decreasing_run": longest_decreasing_run(nums),
        "num_increasing_runs": num_increasing_runs(nums),
        "num_decreasing_runs": num_decreasing_runs(nums),
        "longest_run_values": longest_run_values(nums)
    }
print(analyze_runs([3, 5, 7, 2, 1, 4]))
print(analyze_runs([3, 5, 7, 2, 1, 4]))
print(analyze_runs([1, 2, 3, 4]))
print(analyze_runs([5, 4, 3, 2]))
print(analyze_runs([1, 1, 1]))
print(analyze_runs([4]))
print(analyze_runs([2, 5, 5, 4, 3, 6]))