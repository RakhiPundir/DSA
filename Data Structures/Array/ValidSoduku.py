class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        container = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    data = board[row][col]
                    if (row,data) in container or (data,col) in container or (row//3,col//3,data) in container:
                        return False
                    container.add((row,data))
                    container.add((data,col))
                    container.add((row//3, col//3, data))
        return True
