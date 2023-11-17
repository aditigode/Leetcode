class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        dict1 = {}

        n = len(s)
        maxlength = 0
        for right in range(n):
            if s[right] not in dict1.keys() or dict1[s[right]] < left :
                dict1[s[right]] = right
                maxlength = max(maxlength, (right - left + 1))

            else:
                left = dict1[s[right]] + 1
                dict1[s[right]] = right
            #print(dict1, left, right, maxlength)

        return maxlength



        