class Solution:
    def isMatch(self, text, pattern):
        len_t = len(text)
        len_p = len(pattern)

        # create 2 d array to store result in boolean form
        # M[i][j] is true if text[:i] matches pattern[:j] else false
        M = [[False]*(len_p+1) for i in range(len_t+1)]

        # empty string matches empty pattern, hence true
        M[0][0] = True

        # if pattern has pattern = "d*" and text = "" then compute the result for first row
        for j in range(1,len_p+1):
            if pattern[j-1] == "*" and j > 1:
                M[0][j] = M[0][j-2]

        # construct DP based on previous values
        for i in range(1, len_t+1):
            for j in range(1, len_p+1):
                # if there is a char match or pattern has '.' then skip matching char and copy result
                if pattern[j-1] == "." or text[i-1] == pattern[j-1]:
                    M[i][j] = M[i-1][j-1]
                elif pattern[j-1] == "*":  # if char is '*' then
                    if pattern[j-2] == "." or text[i-1] == pattern[j-2]:
                        # no occurance or one occurance or multiple occurance
                        M[i][j] = M[i][j-1] or M[i-1][j] or M[i][j-2]
                    else:
                        M[i][j] = M[i][j-2]  # no occurence

        return M[-1][-1]