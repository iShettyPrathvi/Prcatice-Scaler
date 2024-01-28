
class Solution:
    # @param A : string
    # @return a strings
    '''You are given a string A of size N.
    Return the string A after reversing the string word by word.
    NOTE:
    A sequence of non-space characters constitutes a word.
    Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
    If there are multiple spaces between words, reduce them to a single space in the reversed string.'''
    def word_reverse(self, A):
        print(type(A), len(A))
        print(A)
        n = len(A)
        char_list = list(A)

        st = 0
        end = n - 1
        while(st<end):
            temp = char_list[st]
            char_list[st] = char_list[end]
            char_list[end] = temp

            st += 1
            end -= 1

        print(''.join(char_list))

        st = 0
        for idx in range(n):
            if char_list[idx] == ' ':
                end = idx - 1 
                while(st<end):
                    temp = char_list[st]
                    char_list[st] = char_list[end]
                    char_list[end] = temp

                    st += 1
                    end -= 1
                
                st = idx + 1 
        
        print(char_list)
        end = n-1
        while(st<end):
            temp = char_list[st]
            char_list[st] = char_list[end]
            char_list[end] = temp

            st += 1
            end -= 1
        
        print(char_list)
        print(len(char_list))
        return ''.join(char_list)




sol = Solution()

A = 'crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv'
res = sol.word_reverse(A)
print(res)


