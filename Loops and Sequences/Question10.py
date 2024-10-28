#Write a function that takes a list of tuples as input,
# where each tuple contains two elements: a string and an integer
# (e.g., ("apple", 5)).
# The function should return a dictionary
# where the strings are the keys and the integers are the values.

def list_of_tuples_to_dict(tuples_list):
    result_dict = {}
    for string, integer in tuples_list:
        result_dict[string] = integer
    return result_dict

# Example usage
example_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
print(list_of_tuples_to_dict(example_list))
