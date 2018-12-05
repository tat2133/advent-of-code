polymer_string = ''
with open('input.txt', 'r') as f:
    polymer_string = f.read().strip()

polymer_list = list(polymer_string)
print(len(polymer_list))

new_polymer_list = []
new_polymer_list.append(polymer_list.pop())
while polymer_list:
    next_char = polymer_list.pop()
    current_char = new_polymer_list.pop()
    if current_char != next_char and (current_char.lower() == next_char or current_char.upper() == next_char):
        continue
    else:
        new_polymer_list.append(current_char)
        new_polymer_list.append(next_char)

print(len(new_polymer_list))
