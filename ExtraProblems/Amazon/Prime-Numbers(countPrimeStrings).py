# https://leetcode.com/discuss/interview-question/593211/count-the-number-of-ways-the-string-can-split-to-get-pime-number

"""
Given a string of length n consisting of digits [0-9], count the number of ways the given string can be split into prime numbers, each of which is in the range 2 to 100 inclusive. Since the answer can be large, return the answer modulo 109 + 7. Note: A partition that contains numbers with leading zeroes will be invalid and the initial string does not contain leading zeroes. Take for example the input string to be s = "11373", then this string can be split into 6 different ways as [11, 37, 3), [113, 7, 3), [11, 3, 73), [11, 37, 3), (113, 73) and [11, 373) where each one of them contains only prime numbers.

Input Format For Custom Testing
The first and only line contains the string, s.
Sample Case 0

Sample Input

For Custom Testing
3175

Sample Output Explanation
The 3 ways to split this string into prime numbers are (31, 7,5), (3, 17, 5), (317,5)
"""

def isPrime(number):
    num = number
    i = 2
    while i * i <= num:
        if ((num % i) == 0):
            return False
        i += 1
    return num > 1

def countPrimeStrings(number, i):
    if (i == 0):
        return 1
    cnt = 0
    for j in range(1, i + 1):
        if (number[i - j] != '0' and isPrime(int(number[i - j: i]))):
            cnt += countPrimeStrings(number, i - j)
    return cnt

if __name__ == "__main__":
    s1 = "3175"
    l1 = len(s1)
    print(countPrimeStrings(s1, l1))
    s2 = "11373"
    l2 = len(s2)
    print(countPrimeStrings(s2, l2))
