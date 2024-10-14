# This challenge asks you to redefine the mysum function we defined in chapter 1, such that it can take any number of arguments. The arguments must all be of the same type and know how to respond to the + operator. (Thus, the function should work with numbers, strings, lists, and tuples, but not with sets and dicts.)

def mysum(*items) -> int:  # using the "splat" operator ( * )
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output


print(mysum())
print(mysum(10, 5, 6, 9))
print(mysum(10, -10, 20, 3))
print(mysum({3, 5}))
print(mysum([2, 4, 4, 3]))
print(mysum('abc', 'def'))
print(mysum([1, 2, 3], [4, 5, 6]))
