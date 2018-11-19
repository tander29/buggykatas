
"""
Katas for codewars, buggy katas
tander29
"""


def build_string(args):
    return "I like {}!".format(", ".join(args))


def quicksort(arr):
    if arr == []:
        return arr
    else:
        p = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < p])
    greater = quicksort([x for x in arr[1:] if x >= p])
    return lesser + [p] + greater


def main():
    print('hello')
    build_string(True)["status"]


if __name__ == "__main__":
    main()
