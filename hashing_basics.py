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
    
    # Do not write code to include libraries, main() function or accept any input from the console.
    # Initialization code is already written and hidden from you. Do not write code for it again.
    # @param A : list of integers
    # @return an integer
    '''Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
    If the given array contains a sub-array with sum zero return 1, else return 0.'''
    def sub_array_zero(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.

        #create prefix sum and if we find a prefix sum which is already present in the dict then return 1
        #else return 0
        n = len(A)
        prefix_sum = [0]*n
        prefix_sum[0] = A[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + A[i]

        prefix_set = set()
        for i in range(n):
            if prefix_sum[i] == 0:
                return 1
            if prefix_sum[i] in prefix_set:
                return 1
            else:
                prefix_set.add(prefix_sum[i])
        return 0
    
    '''Given an integer array A of size N, find the first repeating element in it.
    We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
    If there is no repeating element, return -1.'''
    def find_repeat(self, A):

        n  = len(A)

        itme_freq = {}
        for i in range(n):
            print(i, A[i], itme_freq)
            if A[i] in itme_freq:
                itme_freq[A[i]] += 1
            else:
                itme_freq[A[i]] = 1

        for i in range(n):
            if itme_freq[A[i]] > 1:
                return A[i]

        return -1
    
    '''Given an array A of N integers, return the number of unique elements in the array.'''
    def no_of_unique(self,A):
        n = len(A)
        freq_map = set()
        for i in range(n):
            if A[i] not in freq_map:
                freq_map.add(A[i])
        
        return len(freq_map)


sol = Solution()

A = [6,3,3,6,7,8,7,3,7]
B = [10,9,8]
res = sol.solve(A,B)
print(res)


A = [4, -1, 1]
res = sol.sub_array_zero(A)
print(res)

A = [10,5,3,4,3,5,6]
res = sol.find_repeat(A)
print(res)
A = [6, 10, 5, 4, 9, 120]
res = sol.find_repeat(A)
print(res)

A = [3, 4, 3, 6, 6]
res = sol.no_of_unique(A)
print(res)
A = [3, 3, 3, 9, 0, 1, 0]
res = sol.no_of_unique(A)
print(res)
        
