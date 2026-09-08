"""

Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.

Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.

Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.

link = https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1
"""

def largest(arr):
        # code here
        
        length = len(arr)
        maxi=arr[0]
        
        for i in arr:
            if i > maxi:
                maxi = i

        return maxi

arr = [1, 8, 7, 56, 90]
print(largest(arr))