'''
Insertion Sort

Inseriton Sort is a simple searching algorithm that sorts an array or list by iteratively building up a sorted subarray at the beginning of the array. The algorithm works by dividing the input array into two subarrays: 
* The Sorted Subarray - which contains the first element of the array
* The Unsorted Subarray - which contains the remaining elements of the array

The insertion sort algorithm works as follows:
1. Start with the second element of the array (i) and compare it with the first element (j).
2. If the first element is smaller than the second element, swap them.
3. Move to the next element (new first element in the unsorted array) and insert it into the correct position into the sorted subarray.
4. Repeat step 3 for all remaining elements in the unsorted subarray.

Time Complexity:
* Average, Worst Case Time Complexity: O(n^2)
* Best Case Time Complexity: O(n) - if the input array is already sorted
Space Complexity: O(1)

'''

def insertion_sort(lst):
    for i in range(1, len(lst)): 
        element = lst[i] 
        j = i - 1 
        while j >= 0 and lst[j] > element:
            lst[j+1] = lst[j]
            lst[j] = element
            j -= 1

'''
TRACING

lst = [3,2,5,1]

i   element   j    lst[j]    lst

1     2       0      3       [2,3,5,1]
2     5       1      2       
3     1       2      5       [2,3,1,5]
              1      3       [2,1,3,5]
              0      2       [1,2,3,5]
              -1

'''