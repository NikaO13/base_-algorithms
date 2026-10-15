def partition_lomuto(a: list[int], lo: int, hi: int) -> int:
    pivot = a[hi]
    i = lo - 1

    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    pivot_index = i + 1
    a[pivot_index], a[hi] = a[hi], a[pivot_index]

    return pivot_index


def quick_sort_lomuto(a: list[int]) -> list[int]:

    def sort(lo: int, hi: int) -> None:
        if lo >= hi:
            return

        p = partition_lomuto(a, lo, hi)

        sort(lo, p - 1)
        sort(p + 1, hi)

    sort(0, len(a) - 1)

    return a


a = [12, 65, 2, 30, 80, 24, 12]

print(quick_sort_lomuto(a))