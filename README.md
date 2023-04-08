# Searching and Sorting

# Searching

# Sorting

## Selection Sort

Selection Sort is a simple sorting algorithm that sorts an array or list by repeatedly finding the minimum element from the unsorted part and placing it at the beginning. The algorithm maintains two subarrays in a given array:
* The Sorted Subarray - initially empty
* The Unsorted Subarray - initially the entire array

The selection sort algorithm works as follows: 
1. Find the minimum element in the unsorted subarray.
2. Swap the minimum element with the first element of the unsorted subarray.
3. Move the boundary of the sorted subarray one element to the right.
4. Repeat steps 1 - 3 until the entire array is sorted.

Time Complexity: O(n^2) - two nested for loops are used to sort the array\
Space Complexity: O(1) - sorting is performed in-place (input array is modified)

## Insertion Sort

Inseriton Sort is a simple searching algorithm that sorts an array or list by iteratively building up a sorted subarray at the beginning of the array. The algorithm works by dividing the input array into two subarrays: 
* The Sorted Subarray - which contains the first element of the array
* The Unsorted Subarray - which contains the remaining elements of the array

The insertion sort algorithm works as follows:
1. Start with the second element of the array and compare it with the first element.
2. If the first element is smaller than the second element, swap them.
3. Move to the next element (new first element in the unsorted array) and insert it into the correct position into the sorted subarray.
4. Repeat step 3 for all remaining elements in the unsorted subarray.

Time Complexity:
* Average, Worst Case Time Complexity: O(n^2)
* Best Case Time Complexity: O(n) - if the input array is already sorted
Space Complexity: O(1)