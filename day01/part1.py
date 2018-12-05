frequency = 0

with open('input.txt', 'r') as f:
    for line in f:
        frequency += int(line)

print("final frequency: {}".format(frequency))
