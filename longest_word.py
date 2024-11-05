# Write two functions. find_longest_word takes a filename as an argument and returns the longest word found in the file. The second function, find_all_longest_words, takes a directory name and returns a dict in which the keys are filenames and the values are the longest words from each file.

# Book files are at ~Developer/python_workout/books/*

import os


def find_longest_word(filename):
    longest_word = ""
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word


def find_all_longest_words(dirname):
    # need to return a dict in which the dict's keys are filenames and dict's values are the longest words in each file
    return {filename: find_longest_word(os.path.join(dirname, filename)) for filename in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, filename))}


print(find_all_longest_words('books/.'))
