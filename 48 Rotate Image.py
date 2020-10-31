from typing import List

def rotate(matrix : List[List[int]]) -> None:
    n = len(matrix[0])        
    for i in range(n):
        matrix[i].reverse()
    for i in range(n):
        for j in range(0,n-i):
            matrix[n-1-j][n-1-i], matrix[i][j] = matrix[i][j], matrix[n-1-j][n-1-i] 
        
        
if __name__ == '__main__':
    mymatrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(mymatrix)
    print(mymatrix)