class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        nrow, ncol = len(mat), len(mat[0])
        arr = [0] * (nrow * ncol) 
        ind = 0
        row, col = 0, 0
        top = True  

        while row < nrow and col < ncol:
            if top:
                while row > 0 and col < ncol - 1:
                    arr[ind] = mat[row][col]
                    ind += 1
                    row -= 1
                    col += 1
                arr[ind] = mat[row][col]
                ind += 1
                if col == ncol - 1:
                    row += 1
                else:
                    col += 1
            else:
                while col > 0 and row < nrow - 1:
                    arr[ind] = mat[row][col]
                    ind += 1
                    row += 1
                    col -= 1
                arr[ind] = mat[row][col]
                ind += 1
                if row == nrow - 1:
                    col += 1
                else:
                    row += 1
            top = not top  
        return arr
