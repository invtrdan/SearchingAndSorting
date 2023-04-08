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

Repeat these steps until the entire array is sorted.\

Time Complexity: O(n^2) - two nested for loops are used to sort the array\
Space Complexity: O(1) - sorting is performed in-place (input array is modified)