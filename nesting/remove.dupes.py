# Write a function `remove_dupes(lst)` that accepts a list and returns a new list
# where each element appears only once.

# Example usage:
#print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
#print(remove_dupes([False, False, True, False]))  # [False, True]
#print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]

def remove_dupes(list):
    
    new_list = [list[0]]

    for item in list:
        if not item in new_list:
            new_list.append(item)

    return new_list

remove_dupes(["x", "y", "y", "x", "z"])
remove_dupes([False, False, True, False])
remove_dupes([42, 5, 7, 42, 7, 3, 7, 7])
