def insert(lst: list):
    l = len(lst)
    before = 0
    while before < l - 1:
        wait_insert_index = before + 1
        wait_insert = lst.pop(wait_insert_index)
        have_insert = False
        for i in range(0, before+1):
            if lst[i] > wait_insert:
                lst.insert(i, wait_insert)
                have_insert = True
                break
        if not have_insert:
            lst.insert(before+1, wait_insert)
        before += 1
    return lst


def main():
    l = [3, 2, 1, 8, 7]
    print("charu", insert(l))
    print("charu", insert(l))


if __name__ == "__main__":
    main()
