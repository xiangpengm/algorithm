def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        base = lst[0]
        little = [i for i in lst if i < base]
        big = [i for i in lst if i > base]
        return quick_sort(little) + [base] + quick_sort(big)


def main():
    l = [3, 2, 1, 8, 7]
    print("kuaipai", quick_sort(l))
    print("kuaipai", quick_sort(l))


if __name__ == "__main__":
    main()
