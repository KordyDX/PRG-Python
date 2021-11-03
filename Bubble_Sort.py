def BubbleSort(arr):
    for x in range(0, len(arr) - 1):
        for y in range(0, len(arr) - 1):
            if(arr[y] > arr[y + 1]):
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    return arr

try:
    arr = []
    num = int(input("Input how many values to use.\n"))
    for x in range(1, num + 1):
        arr.append(int(input("Input value(%i)\n" %x)))
    print("List before sorting ", arr)
    print("List after sorting ", BubbleSort(arr))

except ValueError:
    print("Wrong input")
