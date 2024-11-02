# If you run wc against a text file, it’ll count the characters, words, and lines that the file contains.

# The challenge for this exercise is to write a wordcount function that mimics the wc Unix command. The function will take a filename as input and will print four lines of output:

# Number of characters (including whitespace)

# Number of characters (including whitespace)
# Number of words (separated by whitespace)
# Number of lines
# Number of unique words (case sensitive, so “NO” is different from “no”)

def wordcount(file):
    unique_words = set()
    total_chars = 0
    total_words = 0
    total_lines = 0
    with open(file) as f:
        for line in f:
            total_chars += len(line)
            total_lines += 1
            for word in line:
                total_words += 1
                unique_words.add(word)
    print(f"Number of characters: {total_chars}\nTotal words: {
          total_words}\nTotal unique words: {len(unique_words)}\nTotal lines: {total_lines}")


wordcount('wcfile.txt')
