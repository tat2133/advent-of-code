from collections import Counter


def process_claim(line):

    line_elements = line.split(' ')

    claim_id = line_elements[0].lstrip('#')
    dimensions = [int(e) for e in line_elements[-1].split('x')]
    top_left = [int(e) for e in line_elements[-2].rstrip(':').split(',')]

    fabric_locs = []
    for i in range(top_left[0], top_left[0] + dimensions[0]):
        for j in range(top_left[1], top_left[1] + dimensions[1]):
            fabric_locs.append((i, j))

    return claim_id, fabric_locs


fabric_locs = []
claims = []
with open('input.txt', 'r') as f:
    for line in f:
        claim_id, coordinates = process_claim(line)
        fabric_locs.extend(coordinates)
        claims.append([claim_id, coordinates])


square_counter = Counter(fabric_locs)

for claim in claims:
    found = True
    for coordinate in claim[1]:
        if square_counter[coordinate] > 1:
            found = False
            break

    if found:
        break

print("claim with no overlaps: {}".format(claim[0]))

