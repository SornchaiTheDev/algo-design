def binarySearch(list, element):
    listLength = len(list)
    left = 0
    right = len(list) - 1
    while True:
        half = (left + right) // 2
        currentElement = list[half]
        if currentElement > element:
            right = half - 1
        elif currentElement < element:
            left = half + 1
        else:
            print(half)
            break

binarySearch([1,2,3,4,5] , 5)