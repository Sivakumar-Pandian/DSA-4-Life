"""
Sum Except First and Last
Solved

You are given an array arr of numbers. Return the sum of all the elements except the first and last elements.

Examples:

Input: arr[] = [5, 24, 39, 60, 15, 28, 27, 40, 50, 90]
Output: 283
Explanation: The sum of all the elements except the first and last element is 283.

Input: arr[] = [5, 10, 1, 11]
Output: 11
Explanation: The sum of all the elements except the first and last element is 11.

"""

def sumExpect(arr):

    ans = 0
    for i in range(1,len(arr)-1):

        ans += arr[i]
    return ans


arr = [5, 10, 1, 11]

print(sumExpect(arr))