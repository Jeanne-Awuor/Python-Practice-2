#Write a function that takes a dictionary and an integer n as input
# and returns a list of keys from the dictionary
# where the value is greater than n.
# For example, for the dictionary {'a': 5, 'b': 12, 'c': 3} and n = 4,
# the function should return ['a', 'b'].
def keys_with_values_greater_than_n(input_dict, n):
    result = [key for key, value in input_dict.items() if value > n]
    return result

example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_with_values_greater_than_n(example_dict, n))
