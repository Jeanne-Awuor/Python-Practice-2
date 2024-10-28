#Write a Python function that accepts a list of integers and a target sum.
# The function should return True if there are two distinct numbers in the list
# that add up to the target sum, and False otherwise.
def has_pair_with_sum(nums, target_sum):
    seen_numbers = set()
    for num in nums:
        difference = target_sum - num
        if difference in seen_numbers:
            return True
        seen_numbers.add(num)
    return False

# Example usage
example_list = [1,3, 3,5, 5, 7]
target = 4
print(has_pair_with_sum(example_list, target))  # Output: True (3 + 5 = 8)
