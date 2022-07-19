// https://leetcode.com/problems/two-sum/discuss/3/Accepted-Java-O(n)-Solution
// use HashMap to record past nums and quickly find target in one loop
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2]; 
        Map<Integer, Integer> map = new HashMap<Integer, Integer>(); // () in the end
        for(int i =0; i < nums.length; i++){ //length no ()
            if(map.containsKey(target - nums[i])){ // containsKey
                result[1] = i;
                result[0] = map.get(target - nums[i]); // map get and put
                return result;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}