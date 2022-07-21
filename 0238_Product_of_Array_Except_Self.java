//https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space
class Solution {
    public int[] productExceptSelf(int[] nums) {
        // multiple left side first, then multiply right side
        // o(n) time no extra space
        int n = nums.length;
        int[] left = new int[n]; // new arry in Java
        left[0] = 1;
        for(int i= 1; i < n; i++ ){ // from 1 to n-1
            left[i] = left[i-1]*nums[i-1];
        }
        int right = 1;
        for(int i = n-1; i >=0; i--){ // from n-1 to 0
            left[i]*= right;
            right *= nums[i]; // multiply right side
        }
        return left;
    }
}