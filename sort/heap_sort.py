def parent(i):
    return (i + 1) // 2 - 1


def left(i):
    return (i + 1) * 2 - 1


def right(i):
    return 2 * (i + 1)


def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l >= heap_size:
        # 超出数组边界返回
        l = None
    if r >= heap_size:
        r = None
    # 对比左节点和I节点
    if l != None:
        if A[l] > A[i]:
            largest = l
        else:
            largest = i
    else:
        largest = i
    # 对币上面的较大的一个节点与右节点
    if r != None:
        if A[r] > A[largest]:
            largest = r
    # 如果最大节点不为i, 说明堆不符合最大堆
    if largest != i:
        # 交换子节点较大值 到 i 位置
        A[i], A[largest] = A[largest], A[i]
        # log_heap(A)
        max_heapify(A, largest, heap_size)


def build_max_heap(A, heap_size):
    heap_size = len(A)
    for i in range(heap_size//2, -1, -1):
        max_heapify(A, i, heap_size)


def heap(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    index = len(A) - 1
    while index > 0:
        A[0], A[index] = A[index], A[0]
        # print('exchange', index, A)
        heap_size -= 1
        max_heapify(A, 0, heap_size)
        # log_heap(A)
        index -= 1


def main():
    l = [3, 2, 1, 8, 7]
    heap(l)
    print("heap", l)
    heap(l)
    print("heap", l)


if __name__ == "__main__":
    main()
