from string import ascii_lowercase

polymer_string = ''
with open('input.txt', 'r') as f:
    polymer_string = f.read().strip()

polymer_list = list(polymer_string)


def react_polymer(polymer_list):
    new_polymer_list = []
    new_polymer_list.append(polymer_list.pop())
    while polymer_list:
        next_char = polymer_list.pop()
        try:
            current_char = new_polymer_list.pop()
        except IndexError:
            new_polymer_list.append(next_char)
            continue
        if current_char != next_char and (current_char.lower() == next_char or current_char.upper() == next_char):
            continue
        else:
            new_polymer_list.append(current_char)
            new_polymer_list.append(next_char)

    return ''.join(new_polymer_list[::-1])


def remove_unit(polymer_string, unit):
    polymer_string = polymer_string.replace(unit, '')
    polymer_string = polymer_string.replace(unit.upper(), '')

    return polymer_string


reacted = react_polymer(polymer_list)

unit_removed_len = {}

for char in ascii_lowercase:
    removed_polymer = remove_unit(reacted, char)
    unit_removed_len[char] = len(react_polymer(list(removed_polymer)))

for removed_unit, polymer_len in sorted(unit_removed_len.items(), key=lambda x: x[1]):
    print("removed unit {}, length of resulting reacted polymer: {}".format(removed_unit, polymer_len))
