# -*- encoding:utf-8 -*-
from decorator_times import decorator_times

# 取出交集、并集、合集

# numbers_list1 = [1, 2, 3, 4, 5, 6]
# numbers_list2 = [1, 22, 3, 44, 5, 6]


counts = 10000
numbers_list1 = [x for x in xrange(counts)]
numbers_list2 = [x for x in xrange(counts)]


@decorator_times
def list_types():
    # 取并集
    print list(set(numbers_list1 + numbers_list2))
    # 取交集
    union_list = []
    # 取差集
    difference_list = []
    for item1 in numbers_list1:
        if item1 in numbers_list2:
            union_list.append(item1)
        else:
            difference_list.append(item1)
    print union_list
    print difference_list


@decorator_times
def set_types():
    # 集合set()
    numbers_set1 = set(numbers_list1)
    numbers_set2 = set(numbers_list2)

    # 并集
    print numbers_set1.union(numbers_set2)  #等同 |
    # 交集
    print numbers_set1.intersection(numbers_set2)  #等同 &
    # 差集
    print numbers_set1.difference(numbers_set2)  #等同 ^


list_types()
set_types()