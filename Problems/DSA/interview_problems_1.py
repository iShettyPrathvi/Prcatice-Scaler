class Solution:
    # @param A : tuple of integers
    # @return an integer
    '''Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
    You may assume that the array is non-empty and the majority element always exists in the array.'''
    def majorityElement(self, A):

        maj = A[0]
        count = 1

        for i in range(1,len(A)):
            if A[i] == maj:
                count += 1
            else:
                count -= 1

            if count == 0:
                maj = A[i]
                count = 1

        return maj
    
    '''Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.'''
    def longest_ones(self, A):

        n = len(A)
        ans =0

        #edge case
        count = 0
        for i in range(n):
            if A[i] == '1':
                count += 1

        if count == n:
            return n
        if count == 0:
            return 0

        ans = 0
        for i in range(n):
            if A[i] == '0':
                j=i-1
                l=0
                while(j>=0 and A[j] == '1'):
                    l +=1
                    j -= 1

                j=i+1
                r=0
                while(j<n and A[j] == '1'):
                    r += 1
                    j += 1

                curr = l+r+1
                if l+r == count:
                    curr = l+r

                if(curr > ans):
                    ans = curr
        
        return ans

    # @param A : list of list of integers
    # @return a list of list of integers
    '''You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.'''
    def rowMark(self, A, idx):
        for i in range(len(A)):
            if A[idx][i]>0:
                A[idx][i] = -1

    def colMark(sefl,A, idx):
        for i in range(len(A)):
             if A[i][idx]>0:
                 A[i][idx] = -1
        
    def zeroRowCol(self, A):
        n = len(A)
        m = len(A[0])
        # print(n,m)
        for i in range(n):
            for j in range(m):
                if(A[i][j]==0):
                    self.rowMark(A, i)
                    self.colMark(A, j)

        for i in range(n):
            for j in range(m):
                if A[i][j] ==-1:
                    A[i][j] = 0 

        return A

sol = Solution()

A= [2, 1, 2]
res = sol.majorityElement(A)
print(res)

A = "111011101"
res = sol.longest_ones(A)
print(res)
A = "111000"
res = sol.longest_ones(A)
print(res)

# A=[[1,2,3,4],
# [5,6,7,0],
# [9,2,0,4]]
# res = sol.zeroRowCol(A)
# print(res)
A=[[51,21,90,38,57,12,11,1,68,60],[81,24,63,97,75,70,23,91,39,84],[0,21,97,12,46,48,50,3,57,69],[44,8,42,34,99,0,98,10,53,67],[23,34,43,86,31,18,9,54,61,48],[90,61,21,87,26,67,88,28,70,45],[98,14,5,92,1,4,44,99,67,98],[18,42,32,61,80,64,32,89,70,93],[89,61,7,10,0,85,29,40,13,0],[85,63,66,43,56,67,99,0,67,66]]
res = sol.zeroRowCol(A)
print(res)
