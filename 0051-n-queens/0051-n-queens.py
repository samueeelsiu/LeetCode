class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        cols = set()
        diagonals = set()
        anti_diagonals = set()
        board = []

        def backtrack(row: int):
            if row == n:
                res.append(generate_board(board))
                return

            for col in range(n):

                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                board.append(col)

                backtrack(row + 1)
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
                board.pop()
                
        def generate_board(board_state: list[int]) -> list[str]:
            visual_board = []
            for col in board_state:
                row_str = "." * col + "Q" + "." * (n - col - 1)
                visual_board.append(row_str)
            return visual_board
        backtrack(0)
        return res