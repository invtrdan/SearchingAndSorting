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

## Bubble Sort

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

Note:\
* Bubble Sort is NOT very efficient for large arrays.

## Merge Sort

Merge Sort is a popular sorting algorithm that follows the divide-and-conquer approach to sort a list of elements. It works by recursively dividing the unsorted list into smaller sub-lists until each sub-list has only one element. Then, it merges these sub-lists in a sorted order until the entire list is sorted.\

The merge process involves comparing the forst element of each sub-list and selecting the smallest one to be placed in the final sorted list. This process is repeated until all the elements from both sub-lists are merged into the final list.

Time Complexity: O(nlogn)
Space Complexity: O(n+m)

## Quick Sort

QuickSort is a widely used efficient sorting algorithm that uses a divide-and-conquer approach to sort an array of items or elements.\

The basic idea behind QuickSort is to divide the input array into two sub-arrays, one containing all the elements smaller than a pivot element, and the other containing all the elements greater than or equal to the pivot. This process is called partitioning. Once partitioned, QuickSort recursively sorts the two sub-arrays until the entire array is sorted.\

Here are the high-level steps of the QuickSort algorithm:
1. Chose the pivot element from the array.
2. Partition the array around the pivot element, such that all the elements less than the pivot are to the left of the pivot, and all the elements greater than or equal to the pivot are to the right of the pivot.
3. Recursively apply the above two steps to the sub-arrays on the left and right of the pivot until the entire array is sortede.

Time Complexity:
* Average, Best Case Time Complexity: O(nlogn)
* Worst Case Time Complexity: O(n^2)
Space Complexity: O(logn)