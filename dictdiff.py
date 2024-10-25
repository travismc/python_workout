# Write a function, dictdiff, that takes two dicts as arguments. The function returns a new dict that expresses the difference between the two dicts.

# If there are no differences between the dicts, dictdiff returns an empty dict. For each key-value pair that differs, the return value of dictdiff will have a key-value pair in which the value is a list containing the values from the two different dicts. If one of the dicts doesn’t contain that key, it should contain None.

def dictdiff(dict1, dict2):
    output = {}

    for key in dict1:
        if (dict1[key] in dict2) and (dict1[key] != dict2[key]):
            output.update({dict1[key]: [dict]})


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
