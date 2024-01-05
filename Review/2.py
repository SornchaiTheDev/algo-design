A = []

while True:
    value = input()

    if value == "":
        break

    A.append(int(value))

queue = []

for element in A:
    if element > 0:
        queue.append(element)
        continue

    print(element, end=" ")

for element in queue:
    print(element, end=" ")
