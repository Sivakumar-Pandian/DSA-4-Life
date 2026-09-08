"""
Given an integer array arr[], return the sum of all elements of arr.

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.

Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.

link = https://www.geeksforgeeks.org/problems/sum-all-array-elements/

"""


def arraySum(arr):

    count = 0

    for i in arr:
        count += i

    return count

arr = [1, 3, 3]
print(arraySum(arr))