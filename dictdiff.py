# Write a function, dictdiff, that takes two dicts as arguments. The function returns a new dict that expresses the difference between the two dicts.

# If there are no differences between the dicts, dictdiff returns an empty dict. For each key-value pair that differs, the return value of dictdiff will have a key-value pair in which the value is a list containing the values from the two different dicts. If one of the dicts doesn’t contain that key, it should contain None.

# Program Design
# We create an empty output dict.
# We go through each of the keys in first and second.
# For each key, we check if the key also exists in the other dict.
# If the key exists in both, then we check if the values are the same.
# If the values are the same, then we do nothing to output.
# If the values are different, then we add a key-value pair to output, with the currently examined key and a list of the values from first and second.
# If the key doesn’t exist in one dict, then we use None as the value.

def dictdiff(dict1, dict2):
    output = {}  # Create an empty output dict

    for key in dict1:
        if (key in dict2) and (dict1[key] != dict2[key]):
            output.update({key: [dict1[key], dict2[key]]})
        elif (key in dict2) and (dict1[key] == dict2[key]):
            continue
        elif key not in dict2:
            output.update({key: None})

    for key in dict2:
        if (key in dict1) and (dict2[key] != dict1[key]):
            output.update({key: [dict2[key], dict1[key]]})
        elif (key in dict1) and (dict2[key] == dict1[key]):
            continue
        elif key not in dict1:
            output.update({key: None})

    return output


# Example tests
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
print(dictdiff(d1, d1))
print(dictdiff(d1, d2))

d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
print(dictdiff(d3, d4))

d5 = {'a': 1, 'b': 2, 'd': 4}
print(dictdiff(d1, d5))
