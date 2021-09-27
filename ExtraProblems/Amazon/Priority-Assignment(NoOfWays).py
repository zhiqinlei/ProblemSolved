# https://leetcode.com/discuss/interview-question/1362915/amazon-hackerrank-question-priority-assignment
"""
An administrator for Amazon Human Resources has created a queue of all current compliance 
issues along with their priorities. The priorities range from 1 to 99. Create an algorithm that will
reassign priorities so that the value of the maximum priorites so that the value of the maximum poiority assigned is minimized, keeping
the order of priorities between all issues the same

Example
priorities = [1, 4, 8, 4]

There are three priority levels: 1,4 and 8. The array elements are reassigned to priorities [1,2,3,2]
Their order of priorities are maintained while the value of the maximum priority is minimized.

Given the priorities of the issues, return a list that contains the reassigned priority values without reordering.
"""

# We do have an advantage that the range of priorities in [1,99]. thus we can use bucket sort to map the priorities to reduced counts and then reassign the priorities.

# C++ solution
"""
class Solution {
	public int[] reassignPriority (int[] priorities) {
		int[] counts = new int[100];

		for (int priority : priorities) {//count each priority
			counts[priority]++;
		}

		int reducedPriority = 1;
		
		for (int index = 1; index < counts.length; index++) {// reassign the priorities by order
			if (counts[index] > 0){
				counts[index] = reducedPriority++;
			}
		}

		for (int index = 0; index < priorities.length; index++) {
			priorities[index] = counts[priorities[index]];
		}

		return priorities;
	}
}
"""

# time O(n) space O(1)

# another solution
"""
public class AmazonSDE1OA {
    static int noOfWays(int arr[]) {
        int count = 0;
        int n = arr.length;
        int prefix[] = new int[n];
        int suffix[] = new int[n];

        prefix[0] = arr[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + arr[i];
        }

        suffix[n - 1] = arr[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + arr[i];
        }

        for (int i = 0; i < n - 1; i++) {
            if (prefix[i] > suffix[i + 1]) {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        int arr[] = {10, 4, -8, 7};
        System.out.println(noOfWays(arr));
    }
}
"""
