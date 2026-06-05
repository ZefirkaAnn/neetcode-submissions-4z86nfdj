class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if len([board[i][j] for j in range(9) if board[i][j] != "."]) != len(set(''.join(board[i]) + ".")) - 1:
                return False
        
        for i in range(9):
            if len([board[j][i] for j in range(9) if board[j][i] != "."]) != len(set([board[j][i] for j in range(9) if board[j][i] != "."])):
                return False
        
        for k in range(3):
            for i in range(3):
                t = ''.join([''.join(board[i*3+j][k*3:k*3+3]) for j in range(3)])
                if len([t[i] for i in range(9) if t[i]!="."]) != len(set(t+".")) - 1:
                    return False
        return True 