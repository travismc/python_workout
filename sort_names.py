# Write a function, alphabetize_names, that assumes the existence of a PEOPLE constant defined as shown in the code. The function should return the list of dicts, but sorted by last name and then by first name.

# `itemgetter` takes any number of arguments and returns a function that applies each of those arguments in square brackets.

from operator import itemgetter

# phone book data
PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]


def alphabetize_names(people: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(people, key=itemgetter('last', 'first'))


print(alphabetize_names(PEOPLE))
