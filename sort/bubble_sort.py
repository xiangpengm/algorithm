def bubble(lst):
    l = len(lst)
    while l > 0:
        for i in range(l - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        l -= 1
    return lst


def main():
    l = [3, 2, 1, 8, 7]
    print("maopao", bubble(l))


if __name__ == "__main__":
    main()
