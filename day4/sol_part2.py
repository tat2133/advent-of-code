import datetime

from collections import Counter, defaultdict


def process_log_entry(line):

    line_elements = line.split('] ')
    date_string = line_elements[0][1:]
    entry_date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    entry = line_elements[1].strip()

    return entry_date, entry


log_entries = []
with open('input.txt', 'r') as f:
    for line in f:
        log_entries.append(process_log_entry(line))

shifts = []
shift = []
guard = None
for entry in sorted(log_entries):
    if 'begins shift' in entry[1]:
        if guard and len(shift) > 1:
            sleep_intervals = zip(*[iter(shift)]*2)
            shifts.append([guard, sleep_intervals])
        shift = []
        guard = entry[1].split(' ')[1].strip('#')
    else:
        shift.append(entry[0].minute)

sleep_intervals = zip(*[iter(shift)]*2)
shifts.append([guard, sleep_intervals])

guard_sleep_intervals = defaultdict(list)
for shift in shifts:
    guard_sleep_intervals[shift[0]] += list(shift[1])

guard_stats = {}
for guard, sleep_ints in guard_sleep_intervals.items():
    total_sleep_minutes = 0
    minute_list = []
    for sleep_int in sleep_ints:
        total_sleep_minutes += sleep_int[1] - sleep_int[0]
        minute_list.extend([m for m in range(sleep_int[0], sleep_int[1])])

    minute_sleep_frequency = Counter(minute_list)
    most_common_asleep_minute = minute_sleep_frequency.most_common(1)[0]
    guard_stats[guard] = [total_sleep_minutes, most_common_asleep_minute]

for guard, stats in sorted(guard_stats.items(), key=lambda x: x[1][1][1], reverse=True):
    print("guard: {}".format(guard))
    print("minutes asleep: {}".format(stats[0]))
    print("asleep often at minute: {}".format(stats[1]))
    print("guard id x minute most often asleep: {}".format(int(guard) * stats[1][0]))


