class Solution {
    public boolean isPalindrome(String s) {
        char[] c = s.toCharArray(); // trans string into char array
        int i = 0;
        int j = c.length -1;
        while (i < j){ // while loop
            if(!Character.isLetterOrDigit(c[i])){
                //if not letter or digit, skip it
                i++;
            }
            else if (!Character.isLetterOrDigit(c[j])){
                j--;
            }
            else if(Character.toLowerCase(c[i]) != Character.toLowerCase(c[j])){ // trans to lowercase
                return false;
            }
            else{
                i++;
                j--; 
            }
            
        }
        return true;
    }
}