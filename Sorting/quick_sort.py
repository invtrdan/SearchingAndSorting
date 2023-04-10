'''
Quick Sort

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

'''

