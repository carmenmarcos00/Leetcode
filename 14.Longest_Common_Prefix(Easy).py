class Solution(object):
    def longestCommonPrefix(self, strs):
        long_com_pref = []
        strs.sort()                         # Order alphabetically
        first, last = strs[0], strs[-1]     # Get the first and last word (most difference ones)

        
        for i in range(len(first)):                       # Iterate letters of the word
                                                        
            if len(last) > i and last[i] == first[i]:     # If there are still letters to iterate and the actual letter match
                long_com_pref.append(last[i])             #  Then append this letter and keep iterating
            else:
                return ''.join(long_com_pref)             # Finish: no longer o no more similarities
        return ''.join(long_com_pref)
