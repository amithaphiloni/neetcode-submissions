class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i , j  = 0 , 0 
        newword = ""
        while i < len(word1) and i < len(word2):
            newword += word1[i]
            newword += word2[i]
            i += 1
        while i < len(word1):
            newword += word1[i]
            i += 1
        while i < len(word2):
            newword += word2[i]
            i += 1
        return newword