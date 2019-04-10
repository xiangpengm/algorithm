def select(lst):
    l = len(lst)
    start = 0
    while start < l:
        little_index = start
        for i in range(start, l):
            if lst[i] < lst[little_index]:
                little_index = i
        lst[start], lst[little_index] = lst[little_index], lst[start]
        start += 1
    return lst


def main():
    l = [3, 2, 1, 8, 7]
    print("xuanze", select(l))


if __name__ == "__main__":
    main()