'''
Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through a list to be sorted, compares adjacent elements and swaps them if the are in the wrong order. The algorithm gets its name from the way smaller elements "bubble" to the top of the list as the algorithm progresses.

The bubble sort algorithm works as follows:
1. Compare the first two elements of the array. If the first element is greater than the second element, swap them.
2. Move to the next pair of adjacent elements and repeat step 1 for all pairs in the array.
3. Repeat steps 1 and 2 for n-1 passes, where n is the number of elements in the array.
At the end of each pass, the largest element is guaranteed to be in its final sorted position. Therefore, the algorithm can be optimized to stop when no swaps are made during a pass, as this indicates that the list is already sorted.

Time Complexity:
* Average, Worst Case Time Complexity: O(n^2)
* Best Case Time Complexity: O(n)
Space Complexity: O(1)

Note:
* Bubble Sort is NOT very efficient for large arrays.
'''

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] # Swap

'''
TRACING

lst = [3,5,1,2]

i    j    lst[j]  lst[j+1]   lst

0    0      3        5       [3,5,1,2]
     1      5        1       [3,1,5,2]
     2      5        2       [3,1,2,5]
1    0      3        1       [1,3,2,5]
     1      3        2       [1,2,3,5]
2    0      1        2               

'''