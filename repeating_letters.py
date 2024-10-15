# Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return the string that contains the greatest number of repeated letters. In other words

# For each word, find the letter that appears the most times.
# Find the word whose most-repeated letter appears more than any other.

from collections import Counter


words = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


# uses most_repeating_letter_count as key argument for built-in func max
def most_repeating_words(words):
    return max(words, key=most_repeating_letter_count)


print(most_repeating_words(words))
