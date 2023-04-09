'''
Merge Sort

## Merge Sort

Merge Sort is a popular sorting algorithm that follows the divide-and-conquer approach to sort a list of elements. It works by recursively dividing the unsorted list into smaller sub-lists until each sub-list has only one element. Then, it merges these sub-lists in a sorted order until the entire list is sorted.

The merge process involves comparing the forst element of each sub-list and selecting the smallest one to be placed in the final sorted list. This process is repeated until all the elements from both sub-lists are merged into the final list.

Time Complexity: O(nlogn)
Space Complexity: O(n+m)

'''
def merge(lst1, lst2):
    i, j = 0, 0
    res = []
    while i < len(lst1) or j < len(lst2):
        if i >= len(lst1):
            res += lst2[j:]
            break
        elif j >= len(lst1):
            res += lst1[i:]
            break
        elif lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    return res



