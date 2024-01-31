
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
    

    '''Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
    Concatenate the string with itself.
    Delete all the uppercase letters.
    Replace each vowel with '#'.
    You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.
    NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.'''
    def string_modify(self, A):
        n = len(A)
        char_list = list(A)

        #concatenate the string with itself
        char_list += char_list

        #delete all the uppercase letters
        char_list = [c for c in char_list if c.islower()]

        #replace each vowel with '#'
        for idx in range(len(char_list)):
            if char_list[idx] in ['a','e','i','o','u']:
                char_list[idx] = '#'
        
        return ''.join(char_list)
    
    def longestCommonPrefix(self, strings_array):
        if not A:
            return ""

        # Take the first string as the initial prefix
        prefix = A[0]

        # Iterate through the array of strings
        for i in range(1, len(A)):
            j = 0

            # Compare characters of the current string with the prefix
            while j < len(prefix) and j < len(A[i]) and prefix[j] == A[i][j]:
                j += 1

            # Update the prefix based on the common characters
            prefix = prefix[:j]

            # If the prefix becomes empty, no common prefix exists
            if not prefix:
                break

        return prefix
    
    '''You are given a function isalpha() consisting of a character array A.
    Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.'''
    def isAlphNum(self, A):
        n = len(A)
        for i in range(n):
            ch = A[i]
            isalpha =  (ch>= '0' and ch<='9') or (ch>='A' and ch <='Z') or (ch >='a' and ch <= 'z')
            if not isalpha:
                return 0

        return 1




sol = Solution()

A = ' crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv'
res = sol.word_reverse(A)
print(res)

A = ['S','c','a','l','e','r','A','c','a','d','e','m','y','2','0','2','0']
res = sol.isAlphNum(A)
print(res)