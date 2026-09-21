class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        squares = [set() for _ in range(len(board))]

        for r in range(len(rows)):
            for c in range(len(cols)):
                num = board[r][c]

                if num == ".":
                    continue
                
                box_index = (r//3) * 3 + (c//3)

                if num in rows[r] or num in cols[c] or num in squares[box_index]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                squares[box_index].add(num)
        return True