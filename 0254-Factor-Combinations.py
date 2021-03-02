#preium question
'''
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 

Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 

[]
input: 37
output: 

[]
input: 12
output:

[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:

[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
 

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 

Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
 

Examples: 
input: 1
output: 

[]
input: 37
output: 

[]
input: 12
output:

[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:

[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
 写一个函数，给定一个整数n，返回所有可能的因子组合。

解法：递归。从2开始遍历到sqrt(n)，能被n整除就进下一个递归，当start超过sqrt(n)时，start变成n，进下一个递归。
'''
# Time: O(nlogn) Space: O(logn)
class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        result = []
        factors = []
        self.getResult(n, result, factors)
        return result
 
    def getResult(self, n, result, factors):
        i = 2 if not factors else factors[-1]
        while i <= n / i:
            if n % i == 0:
                factors.append(i);
                factors.append(n / i);
                result.append(list(factors));
                factors.pop();
                self.getResult(n / i, result, factors);
                factors.pop()
            i += 1

# more solutions
'''
这道题给了我们一个正整数n，让写出所有的因子相乘的形式，而且规定了因子从小到大的顺序排列，那么对于这种需要列出所有的情况的题目，通常都是用回溯法来求解的，由于题目中说明了1和n本身不能算其因子，那么可以从2开始遍历到n，如果当前的数i可以被n整除，说明i是n的一个因子，将其存入一位数组 out 中，然后递归调用 n/i，此时不从2开始遍历，而是从i遍历到 n/i，停止的条件是当n等于1时，如果此时 out 中有因子，将这个组合存入结果 res 中，参见代码如下：

 

解法一：

复制代码
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        helper(n, 2, {}, res);
        return res;
    }
    void helper(int n, int start, vector<int> out, vector<vector<int>>& res) {
        if (n == 1) {
            if (out.size() > 1) res.push_back(out);
            return;
        }
        for (int i = start; i <= n; ++i) {
            if (n % i != 0) continue;
            out.push_back(i);
            helper(n / i, i, out, res);
            out.pop_back();
        }
    }
};
复制代码
 

下面这种方法用了个小 trick，我们仔细观察题目中给的两个例子的结果，可以发现每个组合的第一个数字都没有超过n的平方根，这个也很好理解，由于要求序列是从小到大排列的，那么如果第一个数字大于了n的平方根，而且n本身又不算因子，那么后面那个因子也必然要与n的平方根，这样乘起来就必然会超过n，所以不会出现这种情况。那么刚开始在2到n的平方根之间进行遍历，如果遇到因子，先复制原来的一位数组 out 为一个新的一位数组 new_out，然后把此因子i加入 new_out，然后再递归调用 n/i，并且从i遍历到 n/i 的平方根，之后再把 n/i 放入 new_out，并且存入结果 res，由于层层迭代的调用，凡是本身能继续拆分成更小因数的都能在之后的迭代中拆分出来，并且加上之前结果，最终都会存 res 中，参见代码如下：

 

解法二：

复制代码
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        helper(n, 2, {}, res);
        return res;
    }
    void helper(int n, int start, vector<int> out, vector<vector<int>> &res) {
        for (int i = start; i <= sqrt(n); ++i) {
            if (n % i != 0) continue;
            vector<int> new_out = out;
            new_out.push_back(i);
            helper(n / i, i, new_out, res);
            new_out.push_back(n / i);
            res.push_back(new_out);
        }
    }
};
复制代码
 

上面两种解法虽有些小不同，但是构成结果的顺序都是相同，对于题目中给的两个例子 n = 12 和 n = 32，结果如下：

 

复制代码
n = 12
2 2 3
2 6
3 4

n = 32
2 2 2 2 2
2 2 2 4
2 2 8
2 4 4
2 16
4 8
复制代码
 

上面两种方法得到的结果跟题目中给的答案的顺序不同，虽然顺序不同，但是并不影响其通过 OJ。下面就给出生成题目中的顺序的解法，这种方法也不难理解，还是从2遍历到n的平方根，如果i是因子，那么递归调用n/i，结果用v来保存，然后新建一个包含i和 n/i 两个因子的序列 out，然后将其存入结果 res, 然后再遍历之前递归 n/i 的所得到的序列，如果i小于等于某个序列的第一个数字，那么将其插入该序列的首位置，然后将序列存入结果 res 中，举个例子，比 n = 12，那么刚开始 i = 2，是因子，然后对6调用递归，得到 {2, 3}，然后此时将 {2, 6} 先存入结果中，然后发现i(此时为2)小于等于 {2, 3} 中的第一个数字2，那么将2插入首位置得到 {2, 2, 3} 加入结果，然后此时i变成3，还是因子，对4调用递归，得到 {2, 2}，此时先把 {3, 4} 存入结果，然后发现i(此时为3)大于 {2, 2} 中的第一个数字2，不做任何处理直接返回，这样就得到正确的结果了：

 

解法三：

复制代码
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        for (int i = 2; i * i <= n; ++i) {
            if (n % i != 0) continue;
            vector<vector<int>> v = getFactors(n / i);
            vector<int> out{i, n / i};
            res.push_back(out);
            for (auto a : v) {
                if (i <= a[0]) {
                    a.insert(a.begin(), i);
                    res.push_back(a);
                }
            }
        }
        return res;
    }
};
复制代码
'''