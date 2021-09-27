# https://leetcode.com/discuss/interview-question/824381/na-amazon-sde-intern-oa-2
"""
Parameters:
scores : List of int
cutOffRank : int
num: int (denoting amount of scores)

You are given a list of integers representing scores of players in a video game. Players can 'level-up' if by the end of the game they have a rank that is at least the cutOffRank. A player's rank is solely determined by their score relative to the other players' scores. For example:

Score : 10 | Rank 1
Score : 5 | Rank 2
Score : 3 | Rank 3
etc.

If multiple players happen to have the same score, then they will all receive the same rank. However, the next player with a score lower than theirs will receive a rank that is offset by this. For example:

Score: 10 | Rank 1
Score: 10 | Rank 1
Score: 10 | Rank 1
Score : 5 | Rank 4

Finally, any player with a score of 0 is automatically ineligible for leveling-up, regardless of their rank.

Return the number of players who are eligible for leveling-up
"""

def cutoffrank(cutoffrank,num,scores):
    scores = sorted(scores,reverse=True)
    while cutoffrank<num:
        if scores[cutoffrank-1]==scores[cutoffrank]:
            cutoffrank+=1
        else:
            return cutoffrank
    return cutoffrank
# scores=[2,2,3,4,5]
scores=[100,50,50,25]
print (cutoffrank(3,4,scores))

# C++ soltuion
"""
public int cutOffRank(int cutOffRank, int num, int[] scores) {
    if(cutOffRank == 0) return 0;
    int[] cache = new int[101];
    for (int n : scores){
        cache[n]++;
    }
    int  res = 0;
    for (int i = 100; i > 0; i--){
        if (cutOffRank <= 0) break;
        cutOffRank -= cache[i];
        res += cache[i];
    }    
    return res;
}
"""