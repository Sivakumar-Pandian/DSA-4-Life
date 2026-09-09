"""
You are given an integer n. You need to convert all zeroes of n to 5.

Examples:

Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.

Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.

"""

def zero2Five(n):

    n = str(n)
    res = ""

    for i in range(len(n)):
        if n[i] == "0":
            res += "5"
        else:
            res += n[i]

    return int(res)

print(zero2Five(1004))