# Write a function called pl_sentence that takes a string containing several words, separated by spaces. (To make things easier, we won’t actually ask for a real sentence. More specifically, there will be no capital letters or punctuation.)


# func to translate word to pig latin
def pig_latin(word: str) -> str:
    if word[0].lower() in 'aeiou':
        return f'{word.lower()}way'

    return f'{word[1:]}{word[0].lower()}ay'


# func to iteratively translate each word in a sentence
def pl_sentence(sentence: str) -> str:
    translated_list = []

    for word in sentence.split():
        translated_list.append(pig_latin(word))

    return " ".join(translated_list)


print(pl_sentence('this is a test translation'))
