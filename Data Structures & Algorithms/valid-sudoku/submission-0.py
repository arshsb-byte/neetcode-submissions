class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxs  = collections.defaultdict(set)

        m = len(board) #rows
        n = len(board[0]) #cols

        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] 
                or board[r][c] in cols[c] or 
                board[r][c] in boxs[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxs[(r//3,c//3)].add(board[r][c])
        return True



        