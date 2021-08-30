# hw1.3.py
# Author(s): Shreejit Verma (shreejiv@andrew.cmu.edu), YingTu(yingt@andrew.cmu.edu)
# Date: 08/13/2021
# 3.a
# rod cutting -- dynamic programming

def price(i):
    if i >= 1 and i <= 4:
        return [0, 1, 5, 8, 9][i]
    return 0

M = {}     # dict of already computed values
C = {0:[], 1:[1], 2:[2], 3:[3]}

def Rev(N):
    if N in M:
        return M[N]
    mxrev = 0
    if N <= 1:
        mxrev = price(N)
    else:
        for k in range(1,N+1):  # [1..N]
            temp = price(k)+Rev(N-k)
            if temp >= mxrev:
                mxrev = temp
                m = k
        C[N] = C[N-m] + C[m]
    M[N] = mxrev
    
    return mxrev

# test code:
if __name__ == '__main__':
    for n in range(0,21):
        print('Rev('+str(n)+'):', Rev(n))
        print('Cut('+str(n)+'):', C[n])

   
# 3.b
# shortest distance algorithm
import numpy as np 
class graph:
    def __init__(self, AdjMatrix0):
        self._AdjMatrix0 = AdjMatrix0
        self.N = len(AdjMatrix0)
        self.M = {}   # dict of already computed matrix        
    
    def SP(self, k):
        # Get k th Adjacency Matrix
        if k in self.M:
            return self.M[k]
        AdjMatrix = np.zeros([self.N,self.N])
        if k == 0:
            AdjMatrix = self._AdjMatrix0
        else:
            for s in range(self.N):
                for t in range(self.N):
                    AdjMatrix[s][t] = min(self.SP(k-1)[s][t], self.SP(k-1)[s][k-1] + self.SP(k-1)[k-1][t])
            self.M[k] = AdjMatrix
        return AdjMatrix

inf = float('inf')
AM1 = [[0,inf,inf,1],
        [2,0,4,5],
        [inf,inf,0,3],
        [inf,7,1,0]]
G1 = graph(AM1) 
G1.SP(4) # final shortest paths matrix

# 3.c
AM2 = [[0,6,inf,1,inf,inf,3],
        [inf,0,2,inf,inf,4,inf],
        [inf,inf,0,4,inf,inf,inf],
        [inf,inf,inf,0,inf,inf,2],
        [inf,inf,1,inf,0,1,inf],
        [inf,inf,4,inf,1,0,inf],
        [2,1,inf,inf,inf,inf,0]]
G2 = graph(AM2) 
G2.SP(7) # final shortest paths matrix



