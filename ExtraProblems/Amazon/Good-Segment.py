"""
Given an Array of bad numbers and a range of integers, how can I determine the longest segment of integers within that inclusive range that doesn't contain a bad number?

For example, you are given the lower limit l = 3 and the upper limit r = 48, The array badNumbers = [37,7,22,15,49,60]. Segments without bad numbers are [3,6], [8,14], [16,21], [23,36] and [38,48]. The longest segment is [23,36] and it is 14 elements long.

Problem : Function Description Complete the function goodStatement in the editor below. The function must return an integer denoting the length of the longest contiguous range of natural number in the range l to r, inclusive, which does not include any bad numbers.

goodSegment has the following parameter(s): badNumbers[badNumbers[0],...badNumbers[n-1]]: an array of integers l: an integer, the lower bound, inclusive r: an integer, the upper bound, inclusive
"""

def goodSegment(lower, badNumbers, upper):
    bad_list = sorted(badNumbers)
    for i, n in enumerate(bad_list):
    # if i % 5000:
    # print(i, '/', len(bad_list), end=' ')
        if n<lower or n>upper:
            badNumbers.remove(n)
    badNumbers.sort()
    diff_lower = badNumbers[0] - lower
    diff_n = []
    for n in range(1, len(badNumbers)):
        diff_n.append(badNumbers[n] - badNumbers[n-1] - 1)
    diff_upper = upper - badNumbers[-1]
    all_diffs = [diff_lower] + diff_n + [diff_upper]
    return max(all_diffs)
