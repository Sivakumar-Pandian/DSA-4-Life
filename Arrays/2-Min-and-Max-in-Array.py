
"""

Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

Examples:

Input: arr[] = [1, 4, 3, 5, 8, 6]
Output: [1, 8]
Explanation: minimum and maximum elements of array are 1 and 8.

Input: arr[] = [12, 3, 15, 7, 9]
Output: [3, 15]
Explanation: minimum and maximum element of array are 3 and 15.

link = https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
"""


def min_and_max(arr):
    mini = arr[0]
    maxi = arr[0]

    for i in arr:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i

    return [maxi, mini]


arr = [1, 4, 3, 5, 8, 6]
print(min_and_max(arr))