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

        longest_prefix = ''
        running_prefix = ''
        last_word = str[0]  # First word is the first last_word

        for word in str[1:]:  # iterate through all of the strings in the list after the first one
            letter_count = 0
            for letter in word:  # iterate through the letters in the word
                if letter != longest_prefix[letter_count] and letter != running_prefix[letter_count]:
                    # If no matches, go to the next word
                    break
                elif letter == longest_prefix[letter_count]:
                    longest_prefix += letter
                    continue
                elif letter == last_word[letter_count] and letter != longest_prefix[letter_count]:



