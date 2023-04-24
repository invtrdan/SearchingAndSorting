'''
Selection Sort

Selection Sort is a simple sorting algorithm that sorts an array or list by repeatedly finding the minimum element from the unsorted part and placing it at the beginning. The algorithm maintains two subarrays in a given array:
* The Sorted Subarray - initially empty
* The Unsorted Subarray - initially the entire array

The selection sort algorithm works as follows: 
1. Find the minimum element in the unsorted subarray.
2. Swap the minimum element with the first element of the unsorted subarray.
3. Move the boundary of the sorted subarray one element to the right.
4. Repeat steps 1 - 3 until the entire array is sorted.

Time Complexity: O(n^2) - two nested for loops are used to sort the array
Space Complexity: O(1) - sorting is performed in-place (input array is modified)
'''

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i] # swapping

'''
TRACING

lst = [5,2,1,4]

i    min_index    j    lst[j]   lst[min_index]   min_index    lst
                                                   (new)
0       0         1      2           5               1         [5,2,1,4]
        1         2      1           2               2         
        2         3      4           1                         [1, 2,5,4]
1       1         2      5           2               
                  3      4           2                         [1,2, 5,4]
2       2         3      4           5               3         [1,2,4, 5]
3
'''
