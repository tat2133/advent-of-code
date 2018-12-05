from collections import Counter


def convert_to_fabric_locs(line):

    line_elements = line.split(' ')

    dimensions = [int(e) for e in line_elements[-1].split('x')]
    top_left = [int(e) for e in line_elements[-2].rstrip(':').split(',')]

    fabric_locs = []
    for i in range(top_left[0], top_left[0] + dimensions[0]):
        for j in range(top_left[1], top_left[1] + dimensions[1]):
            fabric_locs.append((i, j))

    return fabric_locs


fabric_locs = []
with open('test_input.txt', 'r') as f:
    for line in f:
        fabric_locs.extend(convert_to_fabric_locs(line))

square_counter = Counter(fabric_locs)

total_overlap_count = 0

for loc, count in square_counter.most_common():
    if count > 1:
        print("{} {}".format(loc, count))
        total_overlap_count += 1
    else:
        break

print("total squares: {}".format(len(square_counter.keys())))
print("overlap count: {}".format(total_overlap_count))
