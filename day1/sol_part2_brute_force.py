frequency = 0
calibrated = False
frequency_history = set()

while not calibrated:
    with open('input.txt', 'r') as f:
        for line in f:
            frequency += int(line)
            if frequency not in frequency_history:
                frequency_history.add(frequency)
            else:
                calibrated = True
                break

print("calibrated frequency: {}".format(frequency))
