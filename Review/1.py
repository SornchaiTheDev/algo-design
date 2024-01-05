A = []

while True:
    value = input()

    if value == "-1":
        break

    A.append(int(value))

counts = {}

for number in A:
    if number not in counts.keys():
        counts[number] = 1
    else:
        counts[number] += 1

for key, value in counts.items():
    halfCount = len(A) / 2
    if value > halfCount:
        print(key)
