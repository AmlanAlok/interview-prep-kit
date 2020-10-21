#   Array Knowledge Summary

###     1.  When removing duplicates

26  Remove Duplicates from Sorted Array -   https://leetcode.com/problems/remove-duplicates-from-sorted-array/
27  Remove Element -   https://leetcode.com/problems/remove-element/

Use 2 pointers:
    one to check all values (j)
    the other as index to manipulate the same array when a condition is met and then only increment it
    
###     2.  When you need to find an int in an array with unique int values and is unsorted

Approach 1

Do a linear search - Time Complexity = O(n)
    This approach will take more time O(n) but less memory.

Approach 2

First store the array as a hash map using a dictionary.
    d = {v: i for i, v in enumerate(nums)}
    
Check if the value you are looking for is in the dictionary. 
    If yes, use the find key function to get the position of the value.
    This technique is much faster than linear search. Here the time complexity is less but the memory used is more.
    
So, there is trade off. Time vs Memory.


###     3. Binary search implementation to find the position of insertion

        r = len(nums) -1
        l = 0
        mid = 0
        while l <= r:                   # I had missed this line in my first attempt.
            mid = l + ((r - l ) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid -1
        return l        


    