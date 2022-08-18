class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // https://leetcode.com/problems/flood-fill/discuss/109584/Java-9-liner-DFS
        // Time complexity: O(m*n), space complexity: O(1). m is number of rows, n is number of columns.
        if (image[sr][sc] == color) return image;
        fill(image, sr, sc, image[sr][sc], color);
        return image;
    }
    
    public void fill(int[][] image, int sr, int sc, int origincolor, int newcolor){
        if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != origincolor) {
            return;
        }
        image[sr][sc] = newcolor;
        fill(image, sr + 1, sc, origincolor, newcolor);
        fill(image, sr - 1, sc, origincolor, newcolor);
        fill(image, sr, sc + 1, origincolor, newcolor);
        fill(image, sr, sc - 1, origincolor, newcolor);
    }
}