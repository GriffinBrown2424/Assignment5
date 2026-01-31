# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    freq = {}

    for num in numbers:
        freq[num] = freq.get(num, 0) + 1

    return max(freq, key=freq.get)


# Test cases
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
print(most_frequent([5]))
print(most_frequent([2, 2, 1, 1]))

"""
Time and Space Analysis for problem 1:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


# Test cases
print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(remove_duplicates([]))
print(remove_duplicates([1, 1, 1]))

"""
Time and Space Analysis for problem 2:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs


# Test cases
print(find_pairs([1, 2, 3, 4], 5))
print(find_pairs([], 5))
print(find_pairs([2, 4, 6], 10))


"""
Time and Space Analysis for problem 3:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    size = 0
    arr = [None] * capacity

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            new_arr = [None] * (capacity * 2)
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
            capacity *= 2

        arr[size] = i
        size += 1


# Test case
add_n_items(6)

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
- What is the worst-case for a single append?
- What is the amortized time per append overall?
- Space complexity:
- Why does doubling reduce the cost overall?
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    current_sum = 0

    for num in nums:
        current_sum += num
        result.append(current_sum)

    return result


# Test cases
print(running_total([1, 2, 3, 4]))
print(running_total([]))
print(running_total([5]))

"""
Time and Space Analysis for problem 5:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""
