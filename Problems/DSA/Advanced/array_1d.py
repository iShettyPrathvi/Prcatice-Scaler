class Solution:
    '''
    Beggars Outside Temple
    '''
    # @param A : tuple of integers
    # @return an integer
    '''Find the maximum sum of contiguous non-empty subarray within an array A of length N.'''
    #Kadane Algo
    def maxSubArray(self, A):
        n = len(A)

        sub_sum = 0
        ans = -float('inf')

        for i in range(n):
            sub_sum += A[i]
            if(sub_sum > ans):
                ans = sub_sum

            if(sub_sum<=0):
                sub_sum = 0

        return ans
    
    '''There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. 
    Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.
    Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day,
    provided they don't fill their pots by any other means.
    For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, given by the 2D array B'''
    def beggar_sum(self, A, B):
        n=A
        q = len(B)
        beggars = [0]*n

        for i in range(q):
            l = B[i][0] - 1
            r = B[i][1] - 1
            val = B[i][2]

            beggars[l] += val
            #remove contribution after the range
            if(r+1<n):
                beggars[r+1] -= val

        for i in range(1,n):
            beggars[i] = beggars[i-1] + beggars[i]
        
        return beggars
    
    '''Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.'''
    def rain_water_trapped(self, A):
        n = len(A)
        ans = 0
        lmax = 0
        rmax = 0
        i = 0
        j = n-1

        while(i<j):
            lmax = max(lmax, A[i])
            rmax = max(rmax, A[j])

            if(lmax<rmax):
                ans += lmax - A[i]
                i += 1
            else:
                ans += rmax - A[j]
                j -= 1
        
        return ans
    
    def plus_one(self, A):
        n = len(A)
        carry = 1
        for i in range(n-1, -1, -1):
            if(A[i]+carry>9):
                A[i] = 0
                carry = 1
            else:
                A[i] += carry
                carry = 0
                break
        
        if(carry):
            A.insert(0, 1)
        
        while(A[0]==0):
            A.pop(0)
        
        return A
    
    '''You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, 
    such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.
    Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.
    If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. 
    If there are multiple solutions, return the lexicographically smallest pair of L and R.
    NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.'''
    def max_ones(self, A):
        '''
        Using kadane Alogorithm logic
        when ch[i] is '0' and we flip itll become 1 (so effctively adds +1)
        when ch[i] is '1' and we flip itll become 0 (so effctively adds -1)
        so we can find the max sum subarray
        '''

        n = len(A)

        c_sum=0
        max_sum=0
        l=0
        r=0
        ans_ar = [-1]*2

        for i in range(n):
            if(A[i] == "0"):
                c_sum +=1
            else:
                c_sum -= 1

            if c_sum > max_sum:
                max_sum = c_sum
                ans_ar[0] = l+1
                ans_ar[1] = r+1
            
            if c_sum < 0:
                c_sum = 0
                l = i + 1
                r = i + 1
            else:
                r += 1

            if max_sum ==0:
                return []
            else:
                return ans_ar



sol = Solution()
    
# A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
# res = sol.maxSubArray(A)
# print(res)
# A = [1, 2, 3, 4, -10] 
# res = sol.maxSubArray(A)
# print(res)

# A = 10
# B = [[1,3,10],[6,9,2],[3,5,3],[2,8,4],[6,7,5]]
# res = sol.beggar_sum(A, B)
# print(res)

# A = [0, 1, 0, 2]
# res = sol.rain_water_trapped(A)
# print(res)
# A = [1, 2]
# res = sol.rain_water_trapped(A)
# print(res)

# A = [0, 0, 0, 1, 2, 3]
# res = sol.plus_one(A)
# print(res)
# A = [9, 9, 9, 9]
# res = sol.plus_one(A)
# print(res)

A = "010"
res = sol.max_ones(A)
print(res)
A = "111"
res = sol.max_ones(A)
print(res)
