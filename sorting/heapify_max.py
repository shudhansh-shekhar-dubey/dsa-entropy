def heapify_max(list, index):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index

    if left < len(list) and list[left] > list[largest]:
        largest = left

    if right < len(list) and list[right] > list[largest]:
        largest = right

    if largest != index:
        list[index], list[largest] = list[largest], list[index]
        heapify_max(list, largest)


def heap_sort(list):
    sorted = []
    n = len(list)
    heap_size = n
    for i in range((heap_size // 2) - 1, 1, -1):
        heapify_max(list, i)
    for j in range(heap_size - 1, 1, -1):
        list[0], list[j] = list[j], list[0]
        sorted.insert(0,list[j])
        heap_size = heap_size - 1
        heapify_max(list, 1)
    return sorted