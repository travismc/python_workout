# You’ll reimplement the sum (http://mng.bz/MdW2) function that comes with Python. That function takes a sequence of numbers and returns the sum of those numbers. So if you were to invoke sum([1,2,3]), the result would be 6.

# The challenge here is to write a mysum function that does the same thing as the built-in sum function. However, instead of taking a single sequence as a parameter, it should take a variable number of arguments. Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).


def mysum(*numbers) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


print(mysum(10, 5, 6, 9))
print(mysum(10, -10, 20, 3))
print(mysum(*{3, 5}))
print(mysum(*[2, 4, 4, 3]))
