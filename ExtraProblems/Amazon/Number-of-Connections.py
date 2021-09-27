# https://leetcode.com/discuss/interview-question/797541/Amazon-Online-Assessment-2-SDE-1(-New-Graduate-)-2021-(-Coding-2-Questions-)-With-Solutions/659925
"""
第一題是給二維矩陣，計算connection數量
比如
1 0 1
1 1 1
0 1 0
第一層2個node
第二層3個
那麼一二層之間的connection就是2 * 3 = 6
第三層1個
二三層之間connection是3 * 1 = 3
要的是total = 9
"""
def numberOfConnections(gridOfNodes):
    # time complexity O(n^2)
    connections = 0
    if len(gridOfNodes) <= 1:
        return connections
    prev_nodes_sum = sum([x for x in gridOfNodes[0] if x == 1])
    for row in gridOfNodes[1:]:
        curr_nodes_sum = sum([x for x in row if x == 1])
        if curr_nodes_sum > 0:
            connections += prev_nodes_sum * curr_nodes_sum
            prev_nodes_sum = curr_nodes_sum
    return connections
    
grid1 = [[1, 1, 1], [0, 1, 0], [0, 0, 0], [1, 1, 0]]
print(numberOfConnections(grid1)) # 5