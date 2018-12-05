
def is_box_pair(id1, id2):
    mismatch = 0
    for c in range(len(id1)):
        if id1[c] != id2[c]:
            mismatch += 1
            if mismatch > 1:
                return False

    return True


box_ids = []

with open('input.txt', 'r') as f:
    for line in f:
        box_ids.append(line.strip())

found = False
for i in range(len(box_ids) - 1):
    for j in range(i + 1, len(box_ids)):
        found = is_box_pair(box_ids[i], box_ids[j])
        if found:
            break
    if found:
        break

matched_chars = ''
for c in range(len(box_ids[i])):
    if box_ids[i][c] == box_ids[j][c]:
        matched_chars += box_ids[i][c]
print("ids: {}, {}".format(box_ids[i], box_ids[j]))
print("matched chars: {}".format(matched_chars))
