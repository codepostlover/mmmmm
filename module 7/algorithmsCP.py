"""Implementations of some sorting"""
import random
import ArrayList
 
 
def linear_search(a: ArrayList.ArrayList, x):
    for i in range(a.size()):
        if a.get(i) == x:
            return i
    return None
 
 
def binary_search(a: ArrayList.ArrayList, x):
    left = 0
    right = a.size() - 1
    while left <= right:
        mid = (left + right) // 2
        if a.get(mid) == x:
            return mid
        elif x < a.get(mid):
            right = mid - 1
        else:
            left = mid + 1
    return None
 
 
def _merge(a0: ArrayList.ArrayList, a1: ArrayList.ArrayList, a: ArrayList.ArrayList):
    i0 = 0
    i1 = 0
 
    for i in range(a.size()):
        if i0 >= a0.size():
            a.set(i, a1.get(i1))
            i1 += 1
        elif i1 >= a1.size():
            a.set(i, a0.get(i0))
            i0 += 1
        elif a0.get(i0) <= a1.get(i1):
            a.set(i, a0.get(i0))
            i0 += 1
        elif a1.get(i1) < a0.get(i0):
            a.set(i, a1.get(i1))
            i1 += 1
    return
 
 
def merge_sort(a: ArrayList.ArrayList):
    if a.size() <= 1:
        return
    mid = a.size() // 2
    a0 = ArrayList.ArrayList()
    a1 = ArrayList.ArrayList()
    for i in range(mid):
        a0.append(a.get(i))
    for i in range(mid, a.size()):
        a1.append(a.get(i))
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)
    return
 
 
def _partition_f(a :ArrayList, start, end):
    l = start + 1
    r = end
    pivot = a.get(start)
    crossed = False
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l += 1
        while r >= l and a.get(r) >= pivot:
            r -= 1
        if l < r:
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else:
            crossed = True
    a.set(start, a.get(r))
    a.set(r, pivot)
    return r
 
 
def _partition_r(a : ArrayList, start, end):
    idx = random.randint(start, end)
    rand_ele = a.get(idx)
    a.set(idx, a.get(start))
    a.set(start, rand_ele )
    pivot = a.get(start)
    l = start + 1
    r = end
    crossed = False
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l += 1
        while r >= l and a.get(r) >= pivot:
            r -= 1
        if l < r:
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else:
            crossed = True
    a.set(start, a.get(r))
    a.set(r, pivot)
    return r
 
 
def _quick_sort_f(a: ArrayList.ArrayList, start, end):
    if start < end:
        p = _partition_f(a, start, end)
        _quick_sort_f(a, start, p - 1)
        _quick_sort_f(a, p + 1, end)
 
 
def _quick_sort_r(a: ArrayList.ArrayList, start, end):
    if start < end:
        p = _partition_r(a, start, end)
        _quick_sort_r(a, start, p - 1)
        _quick_sort_r(a, p + 1, end)
 
 
def quick_sort(a: ArrayList.ArrayList, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)

 
 