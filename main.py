import os

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        Iterate through the letters in each of the word. If the current running string matches the string from
         the previous word, save that

        """
        answer = ""
        answer = os.path.commonprefix(strs)
        return(answer)