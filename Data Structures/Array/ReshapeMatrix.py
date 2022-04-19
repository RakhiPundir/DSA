class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r*c:
            return mat
        res=[]
        row=[]
        for i in mat:
            for cell in i:
                row.append(cell)
                if len(row)==c:
                    res.append(row)
                    row=[]
        return res  
