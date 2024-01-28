class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    '''Given an array A. You have some integers given in the array B.
    For the i-th number, find the frequency of B[i] in the array A and return a list containing all the frequencies.'''
    def solve(self, A, B):
        print(A)
        print(B)

        n = len(A)

        freq = [0]*len(B)
        print(freq)

        freq_dict = {}


        for i in range(n):
            if A[i] in freq_dict:
                curr_freq = freq_dict[A[i]]
                curr_freq += 1
                freq_dict[A[i]] = curr_freq
            else:
                freq_dict[A[i]] = 1

        for i in range(len(B)):
            if B[i] in freq_dict:
                freq[i] = freq_dict[B[i]]

        return freq


sol = Solution()

A = [6,3,3,6,7,8,7,3,7]
B = [10,9,8]
res = sol.solve(A,B)
print(res)
        
