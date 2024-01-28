class Solution:

    def maxSubarray(self, A, B, C):
        maxSubArrSum = 0
        # create pf
        pf = [0] * len(C)
        pf[0] = C[0]
        for i in range(1, len(C)):
            pf[i] = pf[i - 1] + C[i]
        for i in range(len(C)):
            for j in range(i, len(C)):
                subArrSum = 0
                if i == 0:
                    subArrSum = pf[j]
                else:
                    subArrSum = pf[j] - pf[i - 1]
                if subArrSum > maxSubArrSum and subArrSum <= B:
                    maxSubArrSum = subArrSum
        return maxSubArrSum
    
    # @param A : list of integers
    # @return an long
    def subarraySum(self, A):

        totSum = 0
        array_length = len(A)
        for idx, x in enumerate(A):
            no_of_times = (idx + 1) * (array_length - idx)
            totSum = totSum + no_of_times * x

        return totSum

    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    '''
    Given an array A of length N. Also given are integers B and C.
    Return 1 if there exists a subarray with length B having sum C and 0 otherwise
    '''

    def solve(self, A, B, C):

        n = len(A)
        ans = -float('inf')
        st = 0
        end = B - 1

        sum = 0
        for i in range(0, B):
            sum += A[i]

        if (sum == C):
            return 1

        st += 1
        end += 1

        while (end < n):
            sum = sum - A[st-1] + A[end]
            if (sum == C):
                return 1
            st += 1
            end += 1

        return 0

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    '''Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.'''

    def solveTogether(self, A, B):

        min_swap = 0
        no_of_items_less_b = 0

        for it in A:
            if (it <= B):
                no_of_items_less_b += 1

        window = no_of_items_less_b

        swap = 0

        for idx in range(0, window):
            if A[idx] > B:
                swap += 1

        min_swap = swap

        st = 1
        end = window
        while (end < len(A)):
            if (A[st-1] > B):
                swap -= 1
            if (A[end] > B):
                swap += 1

            min_swap = min(swap, min_swap)
            st += 1
            end += 1

        return min_swap

    # Additional

    def min_average(self, A, B):

        n = len(A)

        window = B

        idx_sub_arr = 0

        sub_sum = 0

        for idx in range(0, window):
            sub_sum += A[idx]

        min_avg = sub_sum/window

        st = 1
        end = window

        while (end < n):
            sub_sum = sub_sum - A[st-1] + A[end]
            curr_avg = sub_sum/window

            if (curr_avg < min_avg):
                min_avg = curr_avg
                idx_sub_arr = st

            st += 1
            end += 1

        return idx_sub_arr, min_avg

    # @return an integer
    '''Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
    1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
    2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
    Your task is to find the count of good subarrays in A.'''

    def good_sub_arr(self, A, B):

        n = len(A)

        good_count = 0

        for i in range(n):
            sub_sum = 0

            for j in range(i, n):
                sub_sum += A[j]
                sub_len = j-i+1
                if sub_len % 2 == 0 and sub_sum < B:
                    good_count += 1

                if sub_sum > B and sub_len % 2 != 0:
                    good_count += 1

        return good_count

    '''Given an array A of N non-negative numbers and a non-negative number B,
    you need to find the number of subarrays in A with a sum less than B.
    We may assume that there is no overflow.'''

    def count_subarrays_with_sum_less_than_b(self, A, B):

        n = len(A)

        sub_sum = 0
        count = 0
        st = 0

        for idx in range(0, n):
            sub_sum += A[idx]

            while (sub_sum >= B):
                sub_sum -= A[st]
                st += 1

            count += idx - st + 1

        return count


result = Solution().subarraySum([2, 9, 5])
print(result)

result = Solution().solve([6, 3, 3, 6, 7, 8, 7, 3, 7], 2, 10)
print(result)

arr = [2255, 6353, 7832, 9990, 516, 9853, 7018, 3337, 3008, 6158, 679, 2954, 2024, 2807, 1944, 6596, 7992, 2942, 9355, 788, 65, 2966, 9276, 1064, 1112, 6197, 4615, 8140, 30, 478, 5360,
       7585, 8853, 9481, 1099, 8781, 9514, 4603, 8209, 7455, 5225, 6740, 4734, 4942, 4475, 4995, 4086, 6448, 1408, 2446, 4675, 92, 4942, 7421,
       6302, 8226, 431, 2463, 5762, 2681, 1877, 2121, 3450, 5930, 9743, 5045, 9977, 906, 9293, 5441, 6825, 3244, 7021, 3910, 7866, 1013, 8227, 7926, 9226, 8710, 7088, 7761, 3413, 4200, 1671, 4526,
       9890, 9594, 257, 3212, 8341, 9641, 2060, 5072, 2776, 4084, 4988, 501, 4304, 3685, 5424, 5713, 7920, 3115, 187, 3915, 3971, 7755, 8802, 4439, 8104, 5610, 5007, 1348, 4449, 9993, 17, 6395, 5539,
       3415, 6500, 9899, 9049, 8197, 1419, 7112, 5823, 4739, 7975, 6915, 5852, 4072, 1694, 4353, 8867, 7362, 3410, 8415, 4060, 1353, 2342, 1712, 9038, 5421, 5772, 9291, 1611, 2822, 7927, 9644, 9236, 6052,
       9592, 2206, 28, 3772, 1694, 2085, 6137, 4683, 655, 4604, 4979, 1948, 661, 9333, 6319, 257, 8146, 5744, 3533, 6508, 6792, 338, 5507, 4191, 7116, 8174, 1577, 1045, 3337, 86, 5667, 9341, 1606, 558,
       7382, 8198, 7954, 225, 7154, 7780, 1290, 1269, 9782, 5909, 6713, 3605, 5672, 8661, 6988, 4669, 1954, 7852, 5580, 5893, 6242, 9970, 2892, 4471, 4272, 3072, 8475, 9925, 8930, 442, 5873, 1128, 2204,
       2384, 3532, 970, 3543, 448, 4699, 2630, 7742, 1563, 1626, 3552, 3030, 3124, 4535, 650, 5330, 3862, 3799, 3011, 7809, 9538, 4567, 6431, 5775, 6903, 6675, 7459, 5750, 4193, 9102, 3352, 4107,
       1483, 7454, 8293, 5044, 9638, 4995, 5558, 9882, 2316, 2614, 9934, 9669, 1486, 762, 4598, 883, 3279, 6893, 1958, 9703, 7636, 5217, 8460, 3711, 2173, 1677, 9273, 1191, 7967, 6001, 9935, 7241,
       2552, 4373, 8518, 2801, 3310, 839, 3715, 7410, 2663, 2894, 1335, 8993, 4987, 6888, 4139, 4324, 4024]
result = Solution().solveTogether(arr, 1732)
print(result)

arr = [3, 7, 90, 20, 10, 50, 40]

result = Solution().min_average(arr, 3)
print(result)
