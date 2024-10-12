# Write a function, firstlast, that takes a sequence (string, list, or tuple) and returns the first and last elements of that sequence, in a two-element sequence of the same type. So firstlast('abc') will return the string ac, while firstlast([1,2,3,4]) will return the list [1,4].


def firstlast(sequence):  # research how to type annotation with multiple types
    return sequence[:1] + sequence[-1:]


print(firstlast([1, 2, 3, 4, 5]))
print(firstlast((1, 2, 3, 4, 5)))
print(firstlast("happy"))
