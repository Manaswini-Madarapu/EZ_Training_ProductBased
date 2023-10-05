import psutil
import time
start_time=time.time()
b4_mem=psutil.virtual_mem().used
n=4
def solve_n_queens(n):
    def is_safe(board,row,col):
     #check left side of crnt row
        for i in range(col):
            if board[row][1]==1:
                return False
        #check upper left diagonal
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        return True
        #check lower left diagonal
        for i,j in zip(range(row,n),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        return True
        def solve(board,col):
            #base case : if all the queens are placed,return True
            if col>=n:
                solns.append(["".join(["q" if x==1 else "." for x in row]) for row in board])
                return True
            for i in range(n):
                if is_safe(board,i,col):
                    board[i][col]=1
                    solve(board,col+1)
                    board[i][col]=0
        solutions=[]
        board[[0]*n for _ in range(n)]
        solve(board,0)
        return solutions
