class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(box):
            ans = [num for num in box if num != '.']
            return len(ans) == len(set(ans))
    '''
    The point is that if we construct a set form set(['1','4','1','5','2']), it will thus construct a collection of unique elements. So adding '1' twice here, does not makes any difference, the result is set(['1', '4', '5', '2']) (or more conveniently written {'1', '4', '5', '2'}). With len(..) we obtain the size of a collection. So the size of that set is the number of unique characters of the input.
    '''
        
        def is_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            return True
        
        def is_col(board):
            for col in zip(*board):
                if not is_valid(col):
                    return False
            return True
        '''
        zip wants a bunch of arguments to zip together, but what you have is a single argument (a list, whose elements are also lists). The * in a function call "unpacks" a list (or other iterable), making each of its elements a separate argument. So without the *, you're doing zip( [[1,2,3],[4,5,6]] ). With the *, you're doing zip([1,2,3], [4,5,6]).
        '''
        def is_box(board):
            for i in (0,3,6):
                for j in (0,3,6):
                    subbox = [board[x][y] for x in range(i, i+3) for y in range (j, j+3)]
                    if not is_valid(subbox):
                        return False
            return True
        
        return is_row(board) and is_col(board) and is_box(board)