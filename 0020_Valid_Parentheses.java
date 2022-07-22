// https://leetcode.com/problems/valid-parentheses/discuss/9178/Short-java-solution
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>(); // Stack
        for (char c: s.toCharArray()){
            // push reverse and check if same nums
            if (c == '('){
                stack.push(')');
            }
            else if (c == '{'){
                stack.push('}');
            }
            else if(c== '['){
                stack.push(']');
            }
            else if(stack.isEmpty() || stack.pop() != c){ // if empty during the loop, false
                return false;
            }
        }
        return stack.isEmpty(); // check if no remaining char
    }
}