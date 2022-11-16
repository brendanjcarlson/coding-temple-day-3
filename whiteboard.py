"""
Find Smallest Number  - (Without min)
Create a function that given a list of numbers (non-sorted) find the lowest number in the list and return it.
Example Input: [50,30,4,2,11,0]
Example Output: 0
Example Input 2: [40,3,4,2]
Example Output 2: 2
"""
from functools import reduce


def lkhdflajgadshf(fasdjlkhfa):
    vzccxczvxc = fasdjlkhfa[0]
    for fdsasdf in set(fasdjlkhfa):
        if vzccxczvxc > fdsasdf:
            vzccxczvxc = fdsasdf
    return vzccxczvxc


def min_without_min(lst):
    s = lst[0]
    for n in lst:
        if s > n:
            s = n
    return s


def with_sort(lst):
    lst.sort()
    return lst[0]


#                        a
lst = [50, 30, 0, 4, 2, -2, 11, 1]
# with reduce

print(reduce(lambda a, c: a if a < c else c, lst))


# print(lkhdflajgadshf(lst))
# print(min_without_min(lst))
# print(with_sort(lst))
