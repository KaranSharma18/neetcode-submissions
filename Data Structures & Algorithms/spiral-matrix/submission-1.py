class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []

        while l < r and t < b:
            
            # Top row
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            
            # right col
            for i in range(t + 1, b + 1):
                res.append(matrix[i][r])
            
            # Bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b][i])
            
            # left col
            for i in range(b - 1, t, -1):
                res.append(matrix[i][l])
            
            l += 1
            r -= 1
            t += 1
            b -= 1
        
        if t == b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
        elif l == r:
            for i in range(t, b + 1):
                res.append(matrix[i][l])
        
        return res

        