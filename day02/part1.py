from collections import Counter

twos = 0
threes = 0

with open('input.txt', 'r') as f:
    for line in f:
        box_id = line.strip()
        char_counts = Counter(box_id).values()

        if 2 in char_counts:
            twos += 1
        if 3 in char_counts:
            threes += 1

print("checksum: {} x {} = {}".format(twos, threes, twos * threes))
