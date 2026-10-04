class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c = len(board), len(board[0])
        rows = [set() for _ in range(r)]
        cols = [set() for _ in range(c)]
        boxes = {}
        
        for i in range(r):
            for j in range(c):
                v = board[i][j]
                
                if v == ".":
                    continue
                
                box = (i //3, j //3)
                boxes.setdefault(box, set())
                
                if v in rows[i] or v in cols[j] or v in boxes[box]:
                    return False
                
                rows[i].add(v)
                cols[j].add(v)
                boxes[box].add(v)
        return True