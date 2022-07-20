//https://leetcode.com/problems/contains-duplicate/discuss/60858/Possible-solutions.
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> distinct = new HashSet<Integer>(); // add new
        for(int num:nums){
            if (distinct.contains(num)){ // contains in set
                return true;
            }
            distinct.add(num); // add in set
        }
        return false;
    }
}