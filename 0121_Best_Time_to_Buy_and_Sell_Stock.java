class Solution {
    public int maxProfit(int[] prices) { // we can prove the answer list must be consecutive increasing
        int cur_max = 0;
        int hist_max = 0;
        for (int i =1; i<prices.length; i++){ // range from 1 to n, < length not length -1
            cur_max = Math.max(0, cur_max + prices[i] - prices[i-1]); // if consecutive increase
            hist_max = Math.max(hist_max, cur_max); // record the max increase in the array
        }
        return hist_max;
    }
}