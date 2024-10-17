# Write a Python function, format_sort_records, that takes the PEOPLE list and returns a formatted string that looks like the following:
# Trump      Donald      7.85
# Putin      Vladimir    3.63
# Xi         Jinping    10.60

from operator import itemgetter


PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


def format_sort_records(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'  # string formatting for template
    for person in sorted(list_of_tuples,
                         key=itemgetter(1, 0)):  # use of itemgetter as key

        output.append(template.format(*person))
    return output


print('\n'.join(format_sort_records(PEOPLE)))
