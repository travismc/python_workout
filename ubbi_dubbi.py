# In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am). In theory, you only put an ub before every vowel sound, rather than before each vowel. Given that this is a book about Python and not linguistics, I hope that you’ll forgive this slight difference in definition.


def ubbi_dubbi(word: str) -> str:
    # letters = word.lower().split('')
    translation = []
    for char in word.lower():
        if char in 'aeiou':
            translation.append(f'ub{char}')
        else:
            translation.append(char)

    return ''.join(translation)


print(ubbi_dubbi('soap'))
print(ubbi_dubbi('Octopus'))
print(ubbi_dubbi('elephant'))
print(ubbi_dubbi('program'))
print(ubbi_dubbi('Milk'))
