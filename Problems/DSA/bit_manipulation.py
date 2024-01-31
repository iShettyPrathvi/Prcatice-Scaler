class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    '''Given two binary strings A and B. Return their sum (also a binary string).'''
    def add_binary(self,A,B):
        # Make both strings of equal length by padding zeros to the left
        max_length = max(len(A), len(B))
        A = A.zfill(max_length)
        B = B.zfill(max_length)

        result = ""
        carry = 0

        # Iterate through the strings from right to left
        for i in range(max_length - 1, -1, -1):
            bit_sum = int(A[i]) + int(B[i]) + carry

            # Update the result string
            result = str(bit_sum % 2) + result

            # Update the carry for the next iteration
            carry = bit_sum // 2

        # If there is a carry after the loop, add it to the left of the result
        if carry:
            result = "1" + result

        return result
		

sol = Solution()

A = '1010110111001101101000'
B = '1000011011000000111100110'
res = sol.add_binary(A,B)
print(res)


		