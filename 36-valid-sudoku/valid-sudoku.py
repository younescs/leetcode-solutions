class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        
        #check rows
        for row in board:
            for element in row:
                if not element.isdigit():
                    continue
                if element in seen:
                    return False
                else: seen.add(element)
            seen.clear()
        
        #check columns
        for column in range(len(board)):
            for row in range(len(board)):
                if not board[row][column].isdigit():
                    continue
                if board[row][column] in seen:
                    return False
                else: seen.add(board[row][column])
            seen.clear()
        
        #check sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if not val.isdigit():
                            continue
                        if val in seen:
                            return False
                        else: seen.add(val)
                seen.clear()

        return True

