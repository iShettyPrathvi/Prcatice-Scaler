
class Solution:
    def diagonal_sum(self, A):
        diag_sum = 0
        row = len(A)

        for i in range(row):
            diag_sum += A[row-i-1][i]

        return diag_sum

        # @return a list of list of integers

    '''Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.'''

    def diagonal(self, A):

        row = len(A)
        col = len(A[0])
        anti_diags = [[0]*row for i in range(row+col-1)]

        ans_row = 0

        for j in range(col):
            r = 0
            c = j
            ans_col = 0
            while (r < row and c >= 0):

                print(f'{ans_row}, {ans_col}')
                anti_diags[ans_row][ans_col] = A[r][c]

                ans_col += 1

                r += 1
                c -= 1
            ans_row += 1

        for i in range(1, row):
            r = i
            c = col - 1
            ans_col = 0
            while (r < row and col >= 0):
                print(f'{ans_row}, {ans_col}')
                anti_diags[ans_row][ans_col] = A[r][c]
                ans_col += 1

                r += 1
                c -= 1

            ans_row += 1

        return anti_diags

     # @param A : list of list of integers
    # @return a list of list of integers
    '''You have to return the Transpose of this 2D matrix.'''

    def mat_transpose(self, A):

        row = len(A)
        col = len(A[0])

        transA = [[0]*row for i in range(col)]

        for i in range(row):
            for j in range(0, col):
                # temp = A[i][j]
                # A[i][j] = A[j][i]
                # A[j][i] = temp
                transA[j][i] = A[i][j]

        return transA
    
    '''
    You are given a n x n 2D matrix A representing an image.
    Rotate the image by 90 degrees (clockwise).
    You need to do this in place.
    Note: If you end up using an additional array, you will only receive partial score.'''
    def rotate90(self, A):
        print(f"Rotate by 90: {A}")
        row = len(A)
        col = len(A[0])

        for i in range(row):
            for j in range(i, col):
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp

        print(A)

        #flip now with colmun
        for i in range(row):
            st = 0
            end = col-1
            while (st<end):
                temp = A[i][st]
                A[i][st] = A[i][end]
                A[i][end] = temp
                st +=1
                end -=1

        return A



arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = Solution().diagonal_sum(arr_2d)
print(res)

arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = Solution().diagonal(arr_2d)
print(res)

arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Transpose")
res = Solution().mat_transpose(arr_2d)
print(res)

arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = Solution().rotate90(arr_2d)
print(res)
