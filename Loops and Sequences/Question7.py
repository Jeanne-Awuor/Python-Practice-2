#Write a function called remove_duplicates that takes a list as input
# and returns a new list with all duplicate elements removed.
# You cannot use the set function to solve this problem.
def remove_duplicates(list1):
    list2= list(dict.fromkeys(list1))
    return list2
lists=[10,10,20,32,10,45]
print(remove_duplicates(lists))
