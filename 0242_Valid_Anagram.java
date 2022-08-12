class Solution {
    public boolean isAnagram(String s, String t) {
        // https://leetcode.com/problems/valid-anagram/discuss/1503603/Java-concise-Single-loop-1-ms-100-beats
        if (s.length() != t.length()){
            return false;
        }
        
        int[] map = new int[26]; // create a 26 size map
        for (int i = 0; i < s.length(); i++){
            map[s.charAt(i) - 'a']++;
            map[t.charAt(i) - 'a']--;
        }
        
        for (int i = 0; i < 26; i++){
            if (map[i] != 0){
                return false;
            }
        }
        
        return true;
    }
}